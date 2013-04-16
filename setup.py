#!/usr/bin/env python

from setuptools import setup

setup(
    name = "stringquery",
    version = "0.0.1",
    author = "Marcin Karkocha",
    author_email = "kivio@kivio.pl",
    description = ("Simple interface to make queries in string data. ",
                  "Something like reversed string format in Python 3.x notation."),
    license = "BSD",
    keywords = "string query reversed format",
    url = "https://github.com/kivio/python-stringquery",
    packages=['stringquery'],
    test_suite='tests',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Filters",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        ],
    )