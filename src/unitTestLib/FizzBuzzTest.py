#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FizzBuzzTest.py
Example simple code for unit test
Use Cases:
- Can I call FizzBuzz
- Get "1" when I pass in 1
- Get "2" when I pass in 2
- Get "Fizz" when I pass in 3
- Get "Buzz" when I pass in 5
- Get "Fizz" when I pass in 6 (multiple of 3)
- Get "Buzz" when i pass in 10 (multiple of 5)
- Get "FizzBuzz" when I pass 15 (multiple of 3 and 5)
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2023/01/18 13:00:00 GMT-6 $
"""

import pytest

def FizzBuzz(value: int) -> str:
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)


def isMultiple(value:int, mod:int) -> bool:
    return (value % mod) == 0


def checkFizzBuzz(value:int, expectedRetVal:str):
    retVal = FizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2WithPassed2In():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")

