# coding: utf-8
from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import spline

train_X = np.linspace(0, 10, 50)
noise = np.random.normal(0, 1, train_X.shape)
train_Y = train_X * 1 - 2 + noise

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(-1., name="weight")
b = tf.Variable(1., name="bias")

activation = tf.add(tf.multiply(X, W), b)

learning_rate = 0.0001

cost = tf.reduce_sum(tf.pow(activation - Y, 2))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

training_epochs = 1000
display_step = 40

c_trace = []
W_trace = []
b_trace = []
activation_trace = []

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})
        if epoch < 10 or epoch % display_step == 0:
            c_tmp = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
            W_tmp = sess.run(W)
            b_tmp = sess.run(b)
            activation_tmp = sess.run(activation, feed_dict={X: train_X})
            print("Epoch: %04d" % (epoch + 1), "cost=", "{:.9f}".format(c_tmp), "W=", W_tmp, "b=", b_tmp)
            c_trace.append(c_tmp)
            W_trace.append(W_tmp)
            b_trace.append(b_tmp)
            activation_trace.append(activation_tmp)
    print("Optimization Finished!")
    print("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}), "W=", sess.run(W), "b=", sess.run(b))

fig, ax = plt.subplots()
l1 = ax.scatter(train_X, train_Y, color='red', label=r'$Original\ data$')
ax.set_xlabel(r'$X\ data$')
ax.set_ylabel(r'$Y\ data$')


def update(i):
    try:
        ax.lines.pop(0)
    except Exception:
        pass
    line, = ax.plot(train_X, activation_trace[i], 'g--', label=r'$Fitting\ line$', lw=2)
    plt.legend(handles=[l1, line], loc='upper center')
    if i == len(activation_trace) - 1:
        ax.text(6, -2, 'Cost: %s' % c_trace[i], fontdict={'size': 16, 'color': 'r'})
        xnew = np.linspace(0, 10, np.max(c_trace) - np.min(c_trace))
        smooth = spline(np.linspace(0, 10, np.size(c_trace)), c_trace, xnew)
        twinax = ax.twinx()
        twinax.set_ylabel(r'Cost')
        costline, = twinax.plot(xnew, smooth, 'b', label=r'$Cost\ line$', lw=2)
        plt.legend(handles=[l1, line, costline], loc='upper center')
    return line,


ani = animation.FuncAnimation(fig, update, frames=len(activation_trace), interval=100)
ani.save('linearregression.gif', writer='imagemagick')

plt.show()
