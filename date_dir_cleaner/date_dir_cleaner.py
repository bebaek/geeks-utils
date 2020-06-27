"""Remove old directories and contents.

Change the parameters in the script. Add a line in crontab as needed:

    0 0 * * * /usr/bin/python3 /home/juni/house-cam/date_dir_cleaner.py

"""

from datetime import date
from pathlib import Path
import shutil

NUM_DAYS = 14


def rm_old_dir(path, num_days):
    """Remove directories in path if they are at least num_days old."""
    today = date.today()

    for d in path.iterdir():
        if not d.is_dir():
            continue

        try:
            d_date = date.fromisoformat(str(d.name))
        except ValueError:
            continue

        diff = (today - d_date).days
        if diff > num_days:
            shutil.rmtree(d)


if __name__ == '__main__':
    HERE = Path(__file__).parent
    rm_old_dir(HERE, num_days=NUM_DAYS)

