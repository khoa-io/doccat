# -*- coding: utf-8 -*-

import os

__all__ = ['DocumentClass', 'TFIDF', 'DocCatError', 'NaiveBayes']
__data_path__ = os.path.join(os.path.dirname(__file__), "data")


class DocCatError(Exception):
	""" Unspecified run-time error. """

	def __init__(self, *args, **kwargs):  # real signature unknown
		pass

	@staticmethod  # known case of __new__
	def __new__(*args, **kwargs):  # real signature unknown
		""" Create and return a new object.  See help(type) for accurate signature. """
		pass
