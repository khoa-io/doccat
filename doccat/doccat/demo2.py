# -*- coding: utf-8 -*-

from doccat.naive_bayes import *

__author__ = "Hoàng Văn Khoa, Vũ Mạnh Kiểm, Lê Anh Thư"

home = "/run/media/p2p/storage/Storage/RVS/khoahv@bitbucket.org/document-classifier"
docat_home = home + os.path.sep + "doccat"
training_path = home + os.path.sep + "training_path"
data_path = docat_home + os.path.sep + "data"
test_path = home + os.path.sep + "test_path"
# test_path = "/run/media/p2p/storage/Temporary/RssVnExpress"
test_file = home + os.path.sep + "test_path/Vnexpress/Phaoluat_vnexpress/Phaoluat_16.txt"

nb = NaiveBayes(data_path)
nb.prepare_to_classify(data_path)

print("=====================================================================================")
print("=====================================================================================")
print("=====================================================================================")
print("=====================================================================================")
print("Kết quả phân loại: ")
# print("{0}: {1}".format(test_file, nb.classify(test_file).name))

D_test = nb.test(test_path)
for entry in D_test:
	print("VB {0}".format(entry))
