""""
import sys
from os.path import dirname, abspath
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
"""
import numpy as np
import matplotlib.pyplot as plt
from os.path import dirname, abspath
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

pwd = "/" + dirname(abspath(__file__))
fstream = open(pwd + "/inputAddress.txt", "r")
inputAddress = fstream.readline()
fstream.close()

mnist = input_data.read_data_sets(inputAddress, one_hot=True)

images = mnist.train.images

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
z = tf.matmul(x, W) + b
y = tf.nn.softmax(z)

yAnswer = tf.placeholder(tf.float32, [None, 10])
learingRate = 0.5
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=z, labels=yAnswer))
trainStep = tf.train.GradientDescentOptimizer(learingRate).minimize(cost)

print("Training")
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

arr = None
before = None

IMG_SHOW = False

for cnt in range(1000):
    batchXs, batchYs = mnist.train.next_batch(100)
    sess.run(trainStep, feed_dict={x:batchXs, yAnswer:batchYs})

    if cnt < 10 and IMG_SHOW:
        try:
            before = arr
        except:
            pass
        arr = sess.run(W).transpose([1, 0])[0].reshape([28, 28])
        fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2)
        ax1.imshow(arr, cmap="gray")
        try:
            diff = abs(arr - before)
            print("max {}" .format(np.ndarray.max(diff)))
            ax2.imshow(diff, cmap="gray")
        except:
            pass
        plt.show()

tf.train.Saver().save(sess, pwd + '/graph_data/mnist_models')


"""
ctcIn3dTBC

bazel build tensorflow/python/tools:freeze_graph && \
bazel-bin/tensorflow/python/tools/freeze_graph \
--input_binary=true \
--input_graph=/home/hohoins/ml/trained/trained.pb \
--input_checkpoint=/home/hohoins/ml/trained/trained.ckpt \
--output_graph=/home/hohoins/ml/trained/frozen_graph.pb --output_node_names=ctcIn3dTBC
"""