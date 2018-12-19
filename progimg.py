#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:45:20 2018

@author: ritwik
"""

import os
import cv2 
path="/home/ritwik/Pictures/ip/misc/"
files=os.listdir(path)
for name in files:
    imgpath=path+name
    img=cv2.imread(imgpath,0)
    imgoutpath="/home/ritwik/Pictures/ip/out2/"+name
    cv2.imwrite(imgoutpath,img)
    #dfg
    