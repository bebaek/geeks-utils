# Security camera image filter

Standalone script to filter security camera images by the presence of detectable
object.

## Prerequisites

- Python 3.6 or higher. For example, install by:

    sudo apt install python3
    
- Use virtual environment if you are not sure:

    sudo apt install python3-venv
    python -m venv ~/_venv/tf2
    source ~/_venv/tf2/bin/activate
    pip install -U pip wheel
    
- (On x86 platform) Tensorflow 2. For example, install by:

    source ~/_venv/tf2/bin/activate
    pip install tensorflow
    
- (On raspbian) Tensorflow lite 2 runtime. Download platform-specific
wheel from the [tensorflow lite guide](https://www.tensorflow.org/lite/guide/python)
and install by:

    pip install <downloaded .whl>
    
- Other python packages:

    pip install Pillow
    
- Optional pip packages:

    pip install flake8
    
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
