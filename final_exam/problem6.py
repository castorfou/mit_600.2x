#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:41:53 2020

@author: explore
"""


import numpy as np


def create_combination(value, maximum):
    """
    value: is a number between 0 and 2**maximum-1
    maximum: a positive int
    
    return a binary representation, as a numpy array, with leading 0 if needed to have len(create_combination)=maximum
    """
    
    string_rep = str(bin(value))[2:]
    #add leading 0
    while (len(string_rep) < maximum):
        string_rep = '0'+string_rep
    return np.array([int(cell) for cell in string_rep])

#maximum = 4
#for i in range(2**maximum):
#    print(create_combination(i, maximum))
    
def get_keys(my_dict, val):
    """
    # function to return keys from my_dict for any value
    #return empty list if no value
    """
    keys=[]
    for key, value in my_dict.items():
         if val == value:
             keys.append(key)
    return keys

def get_minimum_tuple(liste_of_tuple):
    """
    from a list of tuples, return one np.array which sums of items is the minimum
    """
    sum_of_tuple=0
    given_array=0
    for tup in liste_of_tuple:
        arr = np.array(tup)
        if (sum_of_tuple == 0):
            sum_of_tuple = np.sum(arr)
        if (np.sum(arr))<=sum_of_tuple:
            given_array = arr
    return given_array
    
    

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    maximum = len(choices)
    
    dict_results={}
    
    for i in range(2**maximum):
        comb = create_combination(i, maximum)
        product = np.sum(comb*choices)
        if (product-total <=0):
            dict_results[tuple(comb)]=total-product
    
    minimum_value = sorted(set(dict_results.values()))[0]
    print(set(dict_results.values()))
    
    liste_possible = get_keys(dict_results, minimum_value)
    
    
    
    return get_minimum_tuple(liste_possible)
    
    
    
print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3], 5))
print(find_combination([1,1,1,9], 4))
print(find_combination([1, 81, 3, 102, 450, 10], 9))