#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Checkout.py
Features:
- Can call readFromFile
- readFromFile returns correct string
- readFromFile throws exception when file does not exist

--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2024/07/23 13:00:00 GMT-6 $
"""
import os

def readFromFile(filename: str):
    if not os.path.exists(filename):
        raise Exception('Bad File')
    inFile = open(filename, 'r')
    line = inFile.readline()
    return line