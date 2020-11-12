#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:00:43 2020

@author: explore
"""

import numpy as np

listL = [10, 4, 12, 15, 20, 5]
arr = np.array(listL)
print(arr)
print(np.std(arr)/np.mean(arr))