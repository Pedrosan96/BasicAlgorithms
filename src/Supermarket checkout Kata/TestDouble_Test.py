#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TestDoubles_Test.py
Unit test script for doubles in LineReader.py using Mock library
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2024/07/23 13:00:00 GMT-6 $
"""
import pytest
from pytest import raises
from LineReader import readFromFile
from unittest.mock import MagicMock

# def test_canCallReadFromFile():
#     readFromFile('blah')

def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_exists)
    result = readFromFile('blah')
    mock_open.assert_called_once_with('blah', 'r')
    assert result == 'test line'

def test_throwsExceptionWithBadFile(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)
    with raises(Exception):
        result = readFromFile('blah')

