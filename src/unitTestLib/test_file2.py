#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_file2.py
Example simple code for unit test with several examples of fixtures and assert statements
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2023/01/18 13:00:00 GMT-6 $
"""
import pytest

# Test Fixtures allow for re-use of setup and teardown code across tests
# The pytest.fixture decorator is applied to functions that are decorators
# Individual unit test can specify which fixtures they want executed
# The autouse parameter can be set to True to automatically execute a fixture before each test

@pytest.fixture()   # if want to use it for all test set the autouse parameter: @pytest.fixture(autouse=True)
def setup():
    print('\nSetup')


def test1(setup):   # setup function is not called if not send as parameter
    print('Executing test1!')
    assert True


@pytest.mark.usefixtures('setup')      # Decorator to send a setup function
def test2():
    print('Executing test2!')
    assert True

# With the addfinalizer method a teardown method is defined added via the request-context's addfinalizer method
# Multiple finalization functions can be specified

@pytest.fixture()
def setup1():
    print('\nSetup 1')
    yield
    print('\nteardown 1')      # teardown will be called at the end of the test who's applied the setup1

@pytest.fixture()
def setup2(request):
    print('\nSetup 2')

    def teardown_a():
        print('\nTeardown A')

    def teardwon_b():
        print('\nTeardown B')

    request.addfinalizer(teardown_a)    # teardown A will be called at the end, after B, of the test who's applied the setup2
    request.addfinalizer(teardwon_b)


def test3(setup1):
    print('Executing test3')
    assert True

def test4(setup2):
    print('Executing test4')
    assert True


# Test fixtures can have the following four different scopes which specify how often the fixture will be called
    # Function - Run the fixture once for each class of tests
    # Class - Run the fixture once for each class of tests
    # Module - Run once when the module goes in the scope
    # Session - The fixture id run when pytest starts

@pytest.fixture(scope='session', autouse=True)
def setupSession():
    print('\nSetup session')


@pytest.fixture(scope='class', autouse=True)
def setupClass():
    print('\nSetup class!')


@pytest.fixture(scope='module', autouse=True)
def setupModule():
    print('\nSetup Module')


@pytest.fixture(scope='function', autouse=True)
def setupFunction():
    print('\nSetup function')


def test5():
    print('Executing test5!')
    assert True

def test6():
    print('Executing test6!')
    assert True

class TestClass:
    def test_it(self):
        print('TestIt')
        assert True

    def test_it2(self):
        print('TestIt2')
        assert True

# Test fixture return Objects and Params
    # Test fixturecan optionally return data which can be used in the test
    # The optional "params" array argument in the Fixture decorator can be used to specify the data returned to the test
    # When a "params" argument is specified then the test will be called one time with each value specified.


@pytest.fixture(params=[1,2,3])
def setupParams(request):
    retVal = request.param
    print(f'\nSetup! retVal ={retVal}')
    return retVal

def test7(setupParams):
    print(f'\nsetup = {setupParams}')
    assert True


# Pytest allows the use of the built-in python assert statement for performing verifications in a Unit test
# Comparison on all the python data types can be performed using the standard comparison operators:
    # >, <, <=,>=, == and !=
# Pytest expands on the message returned from assert failures to provide more context in the test results

# Validating floating point values can be sometimes difficult as internally the value is a binary fraction (i.e. 1/3 is
# internally 0.333333...)
# Because of this some floating point comparison that would be expected to pass, fail
# The pytest "approx" function can be used to verify that two floating point values are approximately equivalent to each
# other with a default tolerance of 1e-6

# In some cases we want verify that a function throws an exception under certain conditions
# Pytest provides the "raises" helper to perform this verification using the "with" keyword
# If the specified exception is not raised in the code block specified after the "raises" line then the test fails

def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert 'str' == 'str'

def test_floatAssert():
    assert 1.0 == 1.0

def test_arrayAssert():
    assert [1,2,3] == [1,2,3]

def test_dictAssert():
    assert {'1':1} == {'1':1}

def test_float():
    assert (0.1 + 0.2) == pytest.approx(0.3)

def raisesValueException():
    # pass    # raises ValueError
    raise ValueError

def test_exception():
    with pytest.raises(ValueError):
        raisesValueException()