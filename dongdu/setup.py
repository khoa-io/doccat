#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
	from setuptools import setup, find_packages, Extension, distutils
except:
	from distutils.core import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
	name='dongdu',
	version='0.0.1',
	description='Hỗ trợ tách từ dành cho tiếng Việt',
	long_description=''.join(open('README.rst', encoding='UTF-8').readlines()),
	keywords='natural language processing',
	# The project's main homepage.
	url='http://viet.jnlp.org/dongdu',
	author='Lưu Tuấn Anh, Yamamoto Kazuhide',
	author_email='anh@jnlp.org',
	license='GPLv2',
	packages=find_packages(),
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
		'Programming Language :: C++',
	],
	ext_modules=[Extension('dongdu_native', sources=['dongdu/src/DicMap.cpp', 'dongdu/src/Feats.cpp', 'dongdu/src/FeaturesSelection.cpp', 'dongdu/src/Machine.cpp', 'dongdu/src/main.cpp', 'dongdu/src/StrMap.cpp', 'dongdu/src/SylMap.cpp', 'dongdu/src/liblinear/linear.cpp', 'dongdu/src/liblinear/tron.cpp', 'dongdu/src/liblinear/blas/daxpy.cpp', 'dongdu/src/liblinear/blas/ddot.cpp', 'dongdu/src/liblinear/blas/dnrm2.cpp', 'dongdu/src/liblinear/blas/dscal.cpp'], include_dirs=[])],
	include_package_data = True,
	package_data={
		'': ['data/dongdu.map', 'data/dongdu.model', 'data/VNsyl.txt', 'data/wordlist.txt', 'dongdu/src/main.h', 'dongdu/src/configure.h', 'dongdu/src/Feats.h'],
	}
)
