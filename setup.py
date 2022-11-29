#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Fábio P. Fortkamp",
    author_email='fabio@fabiofortkamp.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Explorations from 1st edition (in Portuguese) of Data Science from Scratch, by Joel Grus",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n',
    include_package_data=True,
    keywords='dsdz',
    name='dsdz',
    packages=find_packages(include=['dsdz', 'dsdz.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fabiofortkamp/dsdz',
    version='0.1.0',
    zip_safe=False,
)
