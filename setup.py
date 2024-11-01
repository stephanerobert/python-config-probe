#!/usr/bin/env python
from setuptools import setup


def readme():
    with open('README.md') as read_me:
        return read_me.read()


setup(
    name='config-mixin',
    description='Python Configuration File Helper',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Framework :: tox',
        'Framework :: Pytest',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology'
    ],
    author='Stephane Robert',
    author_email='stephane.robert@gmail.com',
    url='https://github.com/stephanerobert/config-mixin',
    version='1.0.0'
)
