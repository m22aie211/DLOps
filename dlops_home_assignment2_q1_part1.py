# -*- coding: utf-8 -*-
"""DLOps_home_assignment2_q1_part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_zl94YjPG7B2KbZhW4fo80-XdKABVW6A
"""

import numpy as np

def sigmoid(x):
    if isinstance(x, list):
        return [1 / (1 + np.exp(-val)) for val in x]
    else:
        return 1 / (1 + np.exp(-x))

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]
sig_values = sigmoid(random_values)
print(sig_values)