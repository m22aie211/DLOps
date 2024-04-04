# -*- coding: utf-8 -*-
"""DLOps_home_assignment2_q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMBRSc59a1-yJr3MgU_RfVN_f6vK0f7B
"""

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)


def tanh(x):
    return np.tanh(x)


x = np.linspace(-5, 5, 100)
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_leaky_relu = leaky_relu(x)
y_tanh = tanh(x)

print("ReLU :", y_relu)
print("Leaky ReLU :", y_leaky_relu)
print("Tanh :", y_tanh)

plt.figure(figsize=(10, 6))
plt.plot(x, y_sigmoid, label='Sigmoid')
plt.plot(x, y_relu, label='ReLU')
plt.plot(x, y_leaky_relu, label='Leaky ReLU')
plt.plot(x, y_tanh, label='Tanh')
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Activation Functions')
plt.legend()
plt.grid(True)
plt.show()
