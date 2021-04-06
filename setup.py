#! /usr/bin/env python
#
# Copyright (C) 2020-2021 Hakim Moumen

DESCRIPTION = "Hortus: irrigation water management"
LONG_DESCRIPTION = """\
Hortus is a library for irrigation water management in Python.
Here is some of the functionality that hortus offers:
"""

DISTNAME = 'hortus'
MAINTAINER = 'Hakim Moumen'
URL = 'https://hortus.org'
LICENSE = 'Apache 2.0'
DOWNLOAD_URL = 'https://github.com/hmoumen/hortus/'
VERSION = '0.1'
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    'numpy>=1.16',
    'pandas>=0.24',
    'matplotlib>=3.0',
]

EXTRAS_REQUIRE = {
    'all': [
        'scipy>=1.2',
        'statsmodels>=0.9',
    ]
}


PACKAGES = [
    'hortus',
]

CLASSIFIERS = [
    'Intended Audience :: All',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: BSD License',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Multimedia :: Graphics',
    'Operating System :: OS Independent',
    'Framework :: Matplotlib',
]


if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 6):
        raise RuntimeError("hortus requires python >= 3.6.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        maintainer=MAINTAINER,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )