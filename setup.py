#! /usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re
from setuptools import setup


def get_content(name, splitlines=False):
    """Return the file contents with project root as root folder."""

    here = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(here, name)
    with io.open(path, encoding="utf-8") as fd:
        content = fd.read()
    if splitlines:
        content = [row for row in content.splitlines() if row]
    return content


with io.open(os.path.join("wheel", "__init__.py"), encoding="utf-8") as fd:
    # Read version string without importing.
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", fd.read()))

setup(**{
    "name":
        "wheel",
    "version":
        metadata["version"],
    "license":
        "MIT",
    "description":
        "A built-package format for Python",
    "long_description":
        "\n\n".join([
            get_content("README.txt"),
            get_content("CHANGES.txt"),
        ]),
    "url":
        "https://bitbucket.org/pypa/wheel/",
    "author":
        "Daniel Holth",
    "author_email":
        "dholth@fastmail.fm",
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: System :: Archiving :: Packaging",
    ],
    "keywords": [
        "wheel",
        "packaging",
    ],
    "packages": [
        "wheel",
        "wheel.test",
        "wheel.tool",
        "wheel.signatures",
    ],
    "entry_points": """\
[console_scripts]
wheel = wheel.tool:main

[distutils.commands]
bdist_wheel = wheel.bdist_wheel:bdist_wheel
""",
    "zip_safe":
        False,
    "include_package_data":
        True,
    "python_requires":
        ", ".join([
            ">=2.6",
            "!=3.0.*",
            "!=3.1.*",
            "<3.6",
        ]),
    "extras_require": {
        ":python_version=='2.6'": ["argparse"],
        "signatures": ["keyring", "keyrings.alt"],
        "signatures:sys_platform!='win32'": ["pyxdg"],
        "signatures:python_version=='2.6'": ["importlib"],
        "faster-signatures": ["ed25519ll"],
        "tool": [],
    },
    "tests_require":
        get_content("requirements-test.txt", splitlines=True),
})
