import argparse
from datetime import datetime, timedelta
from pathlib import Path
import re
import time

import numpy as np
from PIL import Image, ImageDraw
try:
    from tflite_runtime.interpreter import Interpreter
except ModuleNotFoundError:
    from tensorflow.lite.python.interpreter import Interpreter

HERE = Path(__file__).parent
MODEL_PATH = HERE / Path('data/detect.tflite')
LABEL_PATH = HERE / Path('data/labelmap.txt')
THRESHOLD = 0.4
MIN_NUM_OBJECTS = 1


def secim_filter(
        in_dir,
        out_dir,
        last_minutes,
        model_path=MODEL_PATH,
        label_path=LABEL_PATH, threshold=THRESHOLD,
        min_num_objects=MIN_NUM_OBJECTS,
        show_inference_duration=False,
):
    """Filter images and copy only useful ones."""

    # Get recent image paths to process
    img_paths = _find_recent_images(in_dir, last_minutes)

    # Get labels and model
    labels = _load_labels(label_path)
    interpreter = Interpreter(str(model_path))
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = (
        interpreter.get_input_details()[0]['shape']
    )

    # Iterate over images
    for img_path in img_paths:
        # Read and infer from image
        orig_image = Image.open(img_path)
        image = orig_image.convert('RGB').resize(
            (input_width, input_height), Image.ANTIALIAS)
        start_time = time.monotonic()
        results = _detect_objects(interpreter, image, threshold)
        elapsed_ms = (time.monotonic() - start_time) * 1000
        if show_inference_duration:
            print(elapsed_ms)

        if len(results) < min_num_objects:
            continue

        # Overlay resulting info
        for obj in results:
            ymin, xmin, ymax, xmax = obj['bounding_box']
            _draw_boxes(orig_image, ymin, xmin, ymax, xmax,
                        label=labels[obj['class_id']])

        # Save
        out_path = _get_out_path(img_path, out_dir)
        orig_image.save(out_path, 'JPEG')


def _find_recent_images(root_path, last_minutes, time_by='name'):
    if time_by != 'name':
        raise NotImplementedError

    now = datetime.now()
    delta = timedelta(minutes=last_minutes)

    root_path = Path(root_path)
    all_paths = root_path.glob('**/*.jpg')
    paths_out = []
    for path in all_paths:
        date_str = str(path.parent.name)
        time_str = str(path.stem)
        datetime_str = f'{date_str} {time_str.replace("-", ":")}'
        dt = datetime.fromisoformat(datetime_str)
        if now - dt < delta:
            paths_out.append(path)

    return paths_out


def _load_labels(path):
    """Loads the labels file. Supports files with or without index numbers."""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        labels = {}
        # Somehow labels or model seem to be shifted by 1
        for row_number, content in enumerate(lines[1:]):
            pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
            if len(pair) == 2 and pair[0].strip().isdigit():
                labels[int(pair[0])] = pair[1].strip()
            else:
                labels[row_number] = pair[0].strip()
    return labels


def _detect_objects(interpreter, image, threshold):
    """Returns a list of detection results, each a dictionary of object info.
    """
    _set_input_tensor(interpreter, image)
    interpreter.invoke()

    # Get all output details
    boxes = _get_output_tensor(interpreter, 0)
    classes = _get_output_tensor(interpreter, 1)
    scores = _get_output_tensor(interpreter, 2)
    count = int(_get_output_tensor(interpreter, 3))

    results = []
    for i in range(count):
        if scores[i] >= threshold:
            result = {
                'bounding_box': boxes[i],
                'class_id': classes[i],
                'score': scores[i]
            }
            results.append(result)
    return results


def _set_input_tensor(interpreter, image):
    """Sets the input tensor."""
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image


def _get_output_tensor(interpreter, index):
    """Returns the output tensor at the given index."""
    output_details = interpreter.get_output_details()[index]
    tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
    return tensor


def _get_out_path(in_path, out_root):
    out_root = Path(out_root)
    out_dir = out_root / in_path.parent.name
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / in_path.name


def _draw_boxes(image, ymin, xmin, ymax, xmax, label=''):
    draw = ImageDraw.Draw(image)
    ymin = int(ymin * image.height)
    xmin = int(xmin * image.width)
    ymax = int(ymax * image.height)
    xmax = int(xmax * image.width)
    draw.rectangle((xmin, ymin, xmax, ymax), outline=128, width=2)

    if label:
        draw.text((xmin, ymin), label)


def main():
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='input image root directory')
    parser.add_argument('output_dir', help='output image root directory')
    parser.add_argument('last_minutes', type=int, help='last minutes to look')
    args = parser.parse_args()

    secim_filter(args.input_dir, args.output_dir, args.last_minutes)


if __name__ == '__main__':
    main()
