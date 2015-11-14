# -*- coding: utf-8 -*-
import math
import os
import sys

import dongdu

import doccat.utils

__author__ = "Hoàng Văn Khoa, Vũ Mạnh Kiểm, Lê Anh Thư"


class DocumentClass(object):
	@staticmethod
	def clean_words_list(words_list):
		"""
		Chuẩn hóa các từ chứa trong D_ci
		:param words_list:
		:return:
		"""
		chars = '\b\t\n\f\r\'\"\\`,&!:;?.[](){}/-%^*$#'
		# words = []
		for c in chars:
			# words.append(str(c + "_"))
			for i in range(0, words_list.count(c)):
				words_list.remove(c)

		for i in range(0, words_list.count("._")):
			words_list.remove("._")
		for i in range(0, words_list.count("._.")):
			words_list.remove("._.")
		for i in range(0, words_list.count("._._.")):
			words_list.remove("._._.")

		for w in words_list:
			if any(c.isdigit() for c in w) or len(w) < 3:
				words_list.remove(w)
			w.replace("._", '')
			w.replace("_.", '')
		for w in words_list:
			if any(c.isdigit() for c in w) or len(w) < 3:
				words_list.remove(w)
			w.replace("._", '')
			w.replace("_.", '')
		for w in words_list:
			if any(c.isdigit() for c in w) or len(w) < 3:
				words_list.remove(w)
			w.replace("._", '')
			w.replace("_.", '')

		return words_list

	def __init__(self, name="Unknown", training_path=None, data_file=None):
		"""
		:param name: name of this document class
		:param training_path: folder store document of this class
		:param data_file: file data.txt
		:return:
		"""
		self.data = {}
		self.name = name
		self.D_ci = []
		self.P_ci = 0
		self.words_list = []
		self.__tfidf = None
		self.T_ci = []
		self.training_path = training_path
		self.data_file = data_file
		if training_path is not None:
			self.prepare_to_learn(training_path)
			return
		if data_file is not None:
			self.prepare_to_classify(data_file)

	def prepare_to_learn(self, training_path):
		self.training_path = training_path
		words = ''
		for subdir, dirs, files in os.walk(training_path):
			for file in files:
				file_path = subdir + os.path.sep + file
				shakes = open(file_path, 'r', encoding='utf-8')
				try:
					content = shakes.read()
					words += content
					dk = DocumentClass.clean_words_list(dongdu.segment(content).lower().split())
					self.D_ci.append(dk)
				except:
					print("Cannot read {0}/{1}".format(subdir, file))
					raise RuntimeError("Cannot read {0}/{1}".format(subdir, file))
				print("Read file {0}/{1}".format(subdir, file))
		self.words_list = DocumentClass.clean_words_list(dongdu.segment(words).lower().split())

	def prepare_to_classify(self, data_file):
		data_file = os.path.abspath(data_file)
		self.data_file = data_file
		f = open(data_file, 'r', encoding='utf-8')
		self.data = {}
		self.P_ci = float(f.readline())
		for line in f:
			li = line.split()
			self.data[li[0]] = float(li[1])
		print("Read {0}".format(data_file))
		f.close()

	def tf(self, word):
		return self.words_list.count(word)

	def extract_keywords(self, tfidf):
		keywords_list = []
		for word in doccat.utils.remove_duplicates(self.words_list):
			weight = tfidf.w_tfidf(word, self)
			if weight > 0.65:
				keywords_list.append(word)
		self.T_ci = keywords_list
		return keywords_list

	def cal_P_ci(self, d_size):
		self.P_ci = len(self.D_ci) / d_size
		return self.P_ci

	def cal_P_tj_ci(self, tj, T):
		sum_n_dk_tj = 0
		for dk in self.D_ci:
			sum_n_dk_tj += dk.count(tj)
		sum_n_dk_tm = 0
		for dk in self.D_ci:
			for tm in T:
				sum_n_dk_tm += dk.count(tm)
		return (sum_n_dk_tj + 1) / (sum_n_dk_tm + len(T))


class Document(object):
	def __init__(self, doc_path, T):
		self.likelihoods = {}
		self.T_d = []
		f = open(doc_path, 'r', encoding='utf-8')
		content = f.read()
		f.close()
		self.d = DocumentClass.clean_words_list(dongdu.segment(content).lower().split())
		for w in self.d:
			if w in T:
				self.T_d.append(w)

	def cal_likelihood(self, ci):
		if not isinstance(ci, DocumentClass):
			raise TypeError("ci must be an instance of DocumentClass")
		likelihood_ci = math.log10(ci.P_ci)
		for tj in self.T_d:
			likelihood_ci += math.log10(ci.data[tj])
		self.likelihoods[ci.name] = 0 - likelihood_ci

	def classify(self, C):
		min = sys.float_info.max
		c = C[0]
		for ci in C:
			if self.likelihoods[ci.name] < min:
				min = self.likelihoods[ci.name]
				c = ci
		return c


class TFIDF(object):
	"""
	See https://en.wikipedia.org/wiki/Tf–idf
	"""

	def __init__(self):
		self.dc_list = []

	def add_class(self, dc):
		"""
		Add a class to document classes list
		:param dc:
		:return:
		"""
		if not isinstance(dc, DocumentClass):
			raise TypeError("dc must be a DocumentClass instance")
		if dc in self.dc_list:
			print("Warning: already in this list")
			return False
		# for cls in self.dc_list:
		# 	if cls.class_name is dc.class_name:
		# 		self.dc_list.remove(dc)
		self.dc_list.append(dc)
		return True

	def w_tfidf(self, word, dc):
		"""
		:return: the tf.idf weight of the word in the documents added to this instance
		"""
		if dc not in self.dc_list:
			raise ValueError("Cannot found doc_class in doccls_list")
		w_tf = 0
		if dc.tf(word) > 0:
			w_tf = 1 + math.log10(dc.tf(word))
		if not isinstance(dc, DocumentClass):
			raise TypeError("dc must be an instance of DocumentClass")
		df = 0
		for dc in self.dc_list:
			if word in dc.words_list:
				df += 1
		idf = math.log10(len(self.dc_list) / df)
		return w_tf * idf
