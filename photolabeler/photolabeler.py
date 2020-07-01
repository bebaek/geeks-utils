"""
Simple image class labeler.
"""

from pathlib import Path
import sys

from matplotlib.image import imread
import matplotlib.pyplot as plt

BOLD = '\033[1m'
ENDC = '\033[0m'


def main():
    print(f'{BOLD}Photolabeler{ENDC}')
    print('Type a letter and press Enter. (n: Next, q: Quit)')

    plt.figure(figsize=(6, 6))

    path = Path('images')
    img_paths = sorted(list(path.glob('*.jpg')))

    # Show pics and get user input
    names = []
    labels = []
    for i, name in enumerate(img_paths):
        print(f'{i:4}:', name)
        img = imread(name)
        plt.cla()
        plt.imshow(img)
        plt.pause(0.01)

        while True:
            sys.stdout.write('\a')  # Beep
            sys.stdout.flush()
            inp = input(f'{6 * " "}Class? ([0]/1/n/q) ').lower().strip()
            if inp == '':
                inp = '0'
            if inp in ['0', '1', 'n', 'q']:
                break

        if inp == 'n':
            continue
        if inp == 'q':
            break
        names.append(name.name)
        labels.append(inp)

    if not names:
        print('Nothing to save.')
        return

    # Save
    label_str = (
        '\n'.join([f'{na} {la}' for na, la in zip(names, labels)]) + '\n')
    outfname = 'labels.txt'
    with open(outfname, 'w') as f:
        f.write(label_str)
    print('Saved:', outfname)


if __name__ == '__main__':
    main()
