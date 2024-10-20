#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
commonAlgo.py
--------------------
:author:        Pedrosan96
:version:       $Revision: 0.1 $
:contact:       $linkedin.com/in/pedro-donaldo-sanchez-gal $ (last change)
:date:          $Date: 2023/01/18 13:00:00 GMT-6 $
"""


def binary_search_sorted_iter(array: list, val, l_index: int = 0, r_index: int = None) -> int:
    """
    Iterative binary search of Value in a given sorted Array
    :param array: Given sorted array to search in
    :param l_index: Left index of array
    :param r_index: Right index of array
    :param val: Value to search for
    :return: index of Value in Array, -1 if not found
    """
    if r_index is None:
        r_index = len(array) - 1
    while l_index <= r_index:
        mid = int((l_index + r_index) / 2)
        if val < array[mid]:
            r_index = mid - 1
        elif val > array[mid]:
            l_index = mid + 1
        else:
            return mid
    return -1

def binary_search_sorted_recu(my_array: list, val, l_index: int = 0, r_index: int = None) -> int:
    """
    Iterative binary search of Value in a given sorted Array
    :param my_array: Given sorted array to search in
    :param l_index: Left index of array
    :param r_index: Right index of array
    :param val: Value to search for
    :return: index of Value in Array, -1 if not found
    """
    if r_index is None:
        r_index = len(my_array) - 1
    if not (my_array[l_index] < val > my_array[l_index]):
        return -1
    mid = int((l_index + r_index) / 2)
    if val < my_array[mid]:
        binary_search_sorted_recu(my_array, val, l_index, mid - 1)
    elif val > my_array[mid]:
        binary_search_sorted_recu(my_array, val, mid + 1, r_index)
    else:
        return mid
    return -1


def merge_sort(my_array: list):
    """
    Merge sort algorithm
    :param my_array: Array of numbers to sort
    :return:
    """
    if len(my_array) > 1:
        left_array = my_array[:len(my_array)//2]
        right_array = my_array[len(my_array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i, j, k = 0, 0, 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                my_array[k] = left_array[i]
                i += 1
            else:
                my_array[k] = right_array[j]
                j += 1

            k += 1

        while i < len(left_array):
            my_array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            my_array[k] = right_array[j]
            j += 1
            k += 1

