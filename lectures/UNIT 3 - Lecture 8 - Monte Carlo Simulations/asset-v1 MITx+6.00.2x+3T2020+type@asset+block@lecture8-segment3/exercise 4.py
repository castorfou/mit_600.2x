#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:33:47 2020

@author: explore
"""

import random
import numpy as np

def drawBalls():
    '''
    You have a bucket with 3 red balls and 3 green balls. 
    Assume that once you draw a ball out of the bucket, you don't replace it.
    Return a list of 3 balls: [0, 1, 0]
    0: red, 1: green
    '''
    bucket = [0,0,0,1,1,1]
    result=[]
    for i in range(3):
#        print('tirage '+str(i)+' from bucket ', bucket)
        tirage = random.choice(bucket)
        result.append(tirage)
        bucket.remove(tirage)
#        print('tirage '+str(i)+' result ', result)       
    return result
    
def sameColor(tirage):
    if (np.std(tirage) ==0):
        return True
    return False

def sameColor2(tirage):
    somme=0
    for i in range(len(tirage)):
        somme+=tirage[i]
    if ( (somme ==0) | (somme==3)):
        return True
    return False



def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    estimates = 0
    for t in range(numTrials):
        result_tirage = np.array(drawBalls())
        if (sameColor2(result_tirage)):
            estimates +=1
    return estimates/numTrials
        
        
        
print(drawBalls())
print(noReplacementSimulation(10000))