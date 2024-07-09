#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TestCheckout.py
Unit test script for Checkout.py
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2024/07/08 13:00:00 GMT-6 $
"""
import pytest

from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.additemPrice('a', 1)
    checkout.additemPrice('b', 2)
    return checkout

def test_CanCalculateTotal(checkout):
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)

# @pytest.mark.skip     # Uncomment if want to skip this test
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')