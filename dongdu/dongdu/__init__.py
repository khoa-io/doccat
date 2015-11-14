# -*- coding: utf-8 -*-

__author__ = "Hoàng Văn Khoa"

import os

__data_path__ = os.path.join(os.path.dirname(__file__), "data")

import dongdu_native


def segment(args):
	"""
	Tiến hành tách các từ có trong câu đầu vào
	:param args:
	:return: câu gồm các từ đã được tách
	"""
	if not isinstance(args, str):
		raise TypeError("Input args must be in str!")
	return dongdu_native.segment(args)


def hello(args):
	dongdu_native.hello(args)
