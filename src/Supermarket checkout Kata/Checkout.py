#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Checkout.py
Features:
- Can create instance of Checkout class
- Can add item price
- Can add an item
- Can calculate the current total
- Can add multiple items and get a correct total
- Can add discount rules
- Can apply discount rules to the total
- Exception is thrown for item added without a price
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2024/07/08 13:00:00 GMT-6 $
"""

class Checkout:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount

    def additemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception('Bad item')
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.calculateItemTotalDiscount(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculateItemTotalDiscount(self, item, cnt, discount):
        total = 0
        nbrOfDiscounts = cnt / discount.nbrItems
        total += nbrOfDiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total