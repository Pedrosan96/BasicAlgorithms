#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_file.py
Example simple code for unit test in classes
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2023/01/18 13:00:00 GMT-6 $
"""

import pytest

class TestClass:
    @classmethod
    def setup_class(cls):
        print('Setup TestClass!')

    @classmethod
    def teardown(cls):
        print('Teardown TestClass!')

    def setup_method(self, method):
        if method == self.test1:
            print('Setting up test1!')
        elif method == self.test2:
            print('Setting up test2!')
        else:
            print('Setting up unknown test!')

    def teardown_method(self, method):
        if method == self.test1:
            print('Tearing down test1!')
        elif method == self.test2:
            print('Tearing down test2!')
        else:
            print('Tearing down unknown method')

    def test1(self):
        print('Executing test1')
        assert True

    def test2(self):
        print('Executing test2')
        assert True
