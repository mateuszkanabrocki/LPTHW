try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An example from LPTHW ex46',
    'author': 'Mateusz Kanabrocki',
    'url': 'www.google.pl',
    'download_url': 'Where to download it.',
    'author_email': 'mateusz.kanabrockI@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': ['bin\scriptt1.py'],
    'name': 'ex46'
}

setup(**config)