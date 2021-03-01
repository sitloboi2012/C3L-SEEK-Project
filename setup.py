#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirement = requirements_file.readlines()

setup(
    name="skill_ml_aus",
    version="0.0.1",
    description="Algorithms for Jobs/skills taxonomy creation",
    author="Anh Huy Vo",
    author_email="voyay011@mymail.unisa.edu.au",
    url="https://github.com/sitloboi2012/C3L-SEEK-Project",
    include_package_data = True,
    install_requires = requirement,
    license=None,
)