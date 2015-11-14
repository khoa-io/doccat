# -*- coding: utf-8 -*-

from doccat.naive_bayes import *

home = "/run/media/p2p/storage/Storage/RVS/khoahv@bitbucket.org/document-classifier"
docat_home = home + os.path.sep + "doccat"
training_path = home + os.path.sep + "training_path"
data_path = docat_home + os.path.sep + "data"
test_path = home + os.path.sep + "test_path"
test_file = home + os.path.sep + "test_path/Vnexpress/TheThao_vnexpress/TheThao_19.txt"

nb = NaiveBayes(data_path)
nb.prepare_to_learn(training_path, data_path)
nb.learn()
