#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and
 columns are 0-indexed).

Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
"""
class MySolution:
    def numSpecial(self, mat) -> int:
        counter = 0
        for row in mat:
            if row.count(1)==1:
                idx = row.index(1)
                counter += 1 if [rows[idx] for rows in mat].count(1)==1 else 0

        return counter
