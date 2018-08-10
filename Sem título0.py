#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:04:43 2018

@author: root
"""

def imagetoList(pixels):
    pixels2 = list()
    for k in range(0,len(pixels[:])):
        for j in range(0,len(pixels[0][:])):
            for i in range(0,len(pixels[0][0][:])):
                pixels2.append(pixels[k][j][i])
    return pixels2

def listToImage(lists):
    pixels2 = lists
    pixels = []
    local = 0
    for k in range(0,2):
        for j in range(0,3):
            for i in range(0,3):
                pixels[k][j][i].append(pixels2[local])
                local+=1
    return pixels
                
pixels = [[(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],   [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],   [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],[(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]]
im = imagetoList(pixels)

imasd = listToImage(im)
print(imasd)