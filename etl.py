# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2018-04-24
#
# Copyright (C) 2018 Taishi Matsumura
#
import numpy as np

def load_etl4():
    data = np.load('./etl4.npz')
    x_train = data['x'][:6000]
    y_train = data['y'][:6000]
    x_test = data['x'][6000:]
    y_test = data['y'][6000:]
    return (x_train, y_train), (x_test, y_test)
