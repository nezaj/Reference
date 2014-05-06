#!/usr/bin/env python

from setuptools import setup, find_packages

dependencies = [
    # packages for which we want latest stable version
    "pep8>=1.5.6",
    "pylint>=1.2.1",
    "ipython>=2.0.0",
    "nose>=1.3.2",
    # packages to freeze by default
    "swampy==2.1.7"
]

setup(
    name="think-complexity",
    version="0.1",
    url="https://github.com/nezaj/Reference/tree/master/think_complexity",
    packages=find_packages(),
    install_requires=dependencies
)
