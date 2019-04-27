try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Mateusz Kanabrocki',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mateusz.kanabrockI@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'parser',
    #'name': 'ex49_lexicon',
}

setup(**config)