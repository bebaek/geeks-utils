from setuptools import find_packages, setup

from secim_filter import __version__

setup(
    name='secim_filter',
    version=__version__,
    python_requires='~=3.7',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'secim_filter = secim_filter.__main__:main',
        ],
    },
)
