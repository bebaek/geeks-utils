# Security camera image filter

Standalone script to filter security camera images by the presence of detectable
object.

## Prerequisites

Python 3.6 or higher. For example, install by:

    sudo apt install python3 [python3-dev]
    
Use virtual environment if you are not sure:

    sudo apt install python3-venv
    python3 -m venv ~/_venv/tf2
    source ~/_venv/tf2/bin/activate
    pip install -U pip wheel
    
On x86 platform for dev, Tensorflow 2. For example, install by:

    source ~/_venv/tf2/bin/activate
    pip install tensorflow
    
On raspbian, Tensorflow lite 2 runtime. Download platform-specific
wheel from the [tensorflow lite guide](https://www.tensorflow.org/lite/guide/python)
and install by:

    pip install <downloaded .whl>
    
Other python packages:

    pip install Pillow
    
Optional pip packages:

    pip install flake8
    
## Usage

To see the usage, run the script with `--help` option:

    $ python secim_filter.py --help
    usage: secim_filter.py [-h] [--last-minutes LAST_MINUTES]
                           [--negative-output-dir NEGATIVE_OUTPUT_DIR]
                           input_dir output_dir

    positional arguments:
      input_dir             input image root directory
      output_dir            output image root directory

    optional arguments:
      -h, --help            show this help message and exit
      --last-minutes LAST_MINUTES
                            last minutes to look
      --negative-output-dir NEGATIVE_OUTPUT_DIR
                            negative output image root directory

