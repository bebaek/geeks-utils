import argparse

from .secim_filter import secim_filter


def main():
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_path', help='input image root directory',
        'output_path', help='output image root directory',
        'last_minutes', help='last minutes to look',
    )
    args = parser.parse_args()

    secim_filter(args.input_path, args.output_path, args.last_minutes)


if __name__ == '__main__':
    main()
