# -*- coding: utf-8 -*-
from doccat.document import *

__author__ = "Hoàng Văn Khoa, Vũ Mạnh Kiểm, Lê Anh Thư"


class NaiveBayes(object):

	def __init__(self, data_path):
		self.D = []
		self.tfidf = TFIDF()
		self.d_train = []
		self.T = []
		self.P_tj_ci = []
		self.data_path = data_path

	def prepare_to_learn(self, training_path, data_path):
		"""
		Biểu diễn bài toán
		:param training_path: store classified documents
		:param data_path: store learned data
		:return:
		"""
		self.data_path = data_path
		for subdir in os.listdir(training_path):
			dcp = training_path + os.path.sep + subdir
			dc = DocumentClass(name=subdir, training_path=dcp, data_file=None)
			self.D.append(dc)
			self.tfidf.add_class(dc)
			self.d_train.extend(dc.D_ci)
			if not os.path.exists(data_path + os.path.sep + dc.name):
				os.makedirs(data_path + os.path.sep + dc.name)
				print("Made directory {0}".format(data_path + os.path.sep + dc.name))

	def prepare_to_classify(self, data_path):
		self.data = []
		self.data_path = data_path
		file = open(self.data_path + os.path.sep + 'keywords.txt', 'r', encoding='utf-8')
		print("Read {0}".format(self.data_path + os.path.sep + 'keywords.txt'))
		self.T = file.read().lower().split()
		file.close()
		for subdir, dirs, files in os.walk(data_path):
			if subdir is data_path:
				continue
			dc = DocumentClass(subdir, training_path=None, data_file=subdir + os.path.sep + 'data.txt')
			self.data.append(dc)
		print(self.data)

	def learn(self):
		"""
		GIAI ĐOẠN HỌC
		:return:
		"""
		# Trích ra tập từ khóa T
		global f
		for ci in self.D:
			print("Đang trích xuất từ khóa cho lớp {} . . . ".format(ci.name))
			ci.extract_keywords(self.tfidf)
			print("Những từ đặc trưng cho lớp {}".format(ci.name))
			print(ci.T_ci)
			self.T.extend(ci.T_ci)
		# Lưu lại tập từ khóa này
		f = open(self.data_path + os.path.sep + 'keywords.txt', 'w', encoding='utf-8')
		for ti in self.T:
			f.write("{} ".format(ti))
		f.flush()
		f.close()
		# Đối với mỗi phân lớp cs
		for ci in self.D:
			f = open(self.data_path + os.path.sep + ci.name + os.path.sep + "data.txt", 'w', encoding='utf-8')
			# Tính giá trị xác suất trước của phân lớp c i
			P_ci = ci.cal_P_ci(len(self.d_train))
			f.write("{0}\n".format(P_ci))
			f.flush()
			print("Xác suất trước của phân lớp {0} là {1}".format(ci.name, ci.P_ci))
			# Đối với mỗi từ khóa tj , tính xác suất từ khóa tj xuất hiện đối với lớp ci
			for tj in self.T:
				P_tj_ci = ci.cal_P_tj_ci(tj, self.T)
				print("Xác suất xuất hiện của từ khóa '{0}' trong lớp '{1}' là: {2}".format(tj, ci.name, P_tj_ci))
				f.write("{0} {1}\n".format(tj, P_tj_ci))
				f.flush()
		f.close()

	def classify(self, doc_path):
		doc = Document(doc_path, self.T)
		for ci in self.data:
			doc.cal_likelihood(ci)
		return doc.classify(self.data)

	def test(self, test_path):
		D_test = []
		for subdir, dirs, files in os.walk(test_path):
			for file in files:
				file_path = subdir + os.path.sep + file
				entry = {}
				c = self.classify(file_path)
				entry[file_path] = c.name
				D_test.append(entry)
		return D_test
