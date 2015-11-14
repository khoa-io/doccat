#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

setup(
    name='doccat',
    version='0.0.1',
    description='Chương trình phân loại văn bản Tiếng Việt',
    long_description=''.join(open('README.rst').readlines()),
    keywords='phân loại văn bản Tiếng Việt',
    author='Hoàng Văn Khoa, Vũ Mạnh Kiểm, Lê Anh Thư',
    author_email='hoangvankhoa@outlook.com',
    license='GPLv2',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ]
)
