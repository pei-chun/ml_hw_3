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
   
def kernel_function(xn, xm ,kernel):
    """
        kernel function
        k(xn, xm) = theta0 * exp{-theta1/2 * (|xn - xm|)**2} + theta2 + theta3 * xn.T * xm
    """
    k = kernel[0]
def kernel():
    """
        hyperparameters kernel
    """
    # squared exponential kernel
    kernel_sq = np.asarray([1,4,0,0])
    # linear kernel
    kernel_li = np.asarray([0,0,0,1])
    # exponential-quadratic kernel1
    kernel_ex1 = np.asarray([1,4,0,5])
    # exponential-quadratic kernel2
    kernel_ex2 = np.asarray([1,64,10,0])
    return kernel_sq, kernel_li, kernel_ex1, kernel_ex2

if __name__ == '__main__':
    
    # loading data
    train_x, train_t, test_x, test_t = load()
    
    # initial setting
    kernel_sq, kernel_li, kernel_ex1, kernel_ex2 = kernel()