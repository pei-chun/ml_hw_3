#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:25:35 2017

@author: kathy
"""

import numpy as np
from scipy.io import  loadmat
import matplotlib.pyplot as plt

def load():
    """
        loading training and test data set
    """
    load_data = loadmat('2_data.mat')
    data = load_data['x']
    target = load_data['t']
    train_x, train_t = np.asarray(data[0:60]), np.asarray(target[0:60])
    test_x, test_t = np.asarray(data[60:100]), np.asarray(target[60:100])
    
    return train_x, train_t, test_x, test_t

if __name__ == '__main__':
    
    # loading data
    train_x, train_t, test_x, test_t = load()