# Security camera image filter

Standalone script to filter security camera images by the presence of detectable
object.

## Prerequisites

- Python 3.6 or 3.7
- Tensorflow lite 2. Install platform-specific wheel from the
[guide](https://www.tensorflow.org/lite/guide/python)

## Usage

To see the usage, run the script with `--help` option:

    $ python secim_filter.py --help
    usage: secim_filter.py [-h] input_path output_path last_minutes

    positional arguments:
      input_path    input image root directory
      output_path   output image root directory
      last_minutes  last minutes to look

    optional arguments:
      -h, --help    show this help message and exit
