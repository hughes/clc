try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'clc - the Command Line Calculator',
    'author': 'Matt Hughes',
    'version': '0.1',
    'packages': ['clc'],
    'scripts': [],
    'entry_points': {
        'console_scripts': ['clc = clc.main:main']
    },
    'name': 'clc',
    'test_suite': 'tests'
}

setup(**config)
