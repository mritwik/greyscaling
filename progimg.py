#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:45:20 2018

@author: ritwik
"""


import os
import cv2 


path=" ...input folder containing images should replace this text... "
#NOTE: In windows, pls replace all slashes('/') with double slashes

files=os.listdir(path)

for name in files:
    imgpath=path+name
    img=cv2.imread(imgpath,0)
    imgoutpath="  ...output destination folder should should replace this...  "+name
    #NOTE: In windows, pls replace all slashes('/') with double slashes
    cv2.imwrite(imgoutpath,img)
