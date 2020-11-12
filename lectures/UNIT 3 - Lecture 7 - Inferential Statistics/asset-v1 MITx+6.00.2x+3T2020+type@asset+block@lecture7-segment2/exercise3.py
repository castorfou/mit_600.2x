#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:46:22 2020

@author: explore
"""

import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if (len(L)==0):
        return math.nan


    Llen = [len(a) for a in L]
    moyenne=(sum(Llen)/len(Llen))
    std = 0
    for i in range(len(Llen)):
        std+=(Llen[i]-moyenne)**2
    std/=len(Llen)
    std=math.sqrt(std)
    return std

L = ['a', 'z', 'p']
print(stdDevOfLengths(L))

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))

print(stdDevOfLengths([]))
