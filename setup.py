#! /usr/bin/env python3.9
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='pelothon',
    version='0.0.1',
    author='Paul Norton',
    license='LICENSE.txt',
    description='Peloton unofficial API Integration for Home Automation',
    packages=[pelothon]
)
