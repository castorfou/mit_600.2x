#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:33:30 2020

@author: explore
"""

import random

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

def sameColor2(tirage):
    somme=0
    for i in range(len(tirage)):
        somme+=tirage[i]
    if ( (somme ==0) | (somme==3)):
        return True
    return False

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    all_same_color = 0
    for drawing_exp in range(1, numTrials+1):
        result_tirage = drawBalls()
        if (sameColor2(result_tirage)):
            all_same_color +=1
    return all_same_color/numTrials


