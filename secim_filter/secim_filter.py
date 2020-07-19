import argparse
from datetime import datetime, timedelta
from pathlib import Path


def secim_filter(in_path, out_path, last_minutes):
    """Filter images and copy only useful ones."""

    # Get recent image paths to process
    img_paths = _find_recent_images(in_path, last_minutes)
    print(img_paths)

    # Iterate over images

        # Read

        # Run object detection on each

        # Save

    return


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


def main():
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', help='input image root directory')
    parser.add_argument('output_path', help='output image root directory')
    parser.add_argument('last_minutes', type=int, help='last minutes to look')
    args = parser.parse_args()

    secim_filter(args.input_path, args.output_path, args.last_minutes)


if __name__ == '__main__':
    main()
