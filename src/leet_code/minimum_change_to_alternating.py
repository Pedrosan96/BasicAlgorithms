#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1'
 or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating,
 while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
"""


class MySolution:
    def minOperations(self, s: str) -> int:
        counter_1, counter_0 = 0, 0
        one, zero = 1, 0
        s_len = len(s)
        if s_len%2 != 0:
            counter_1 += 1 if (int(s[-1])+ one)==1 else 0
            counter_0 += 1 if (int(s[-1])+ zero)==1 else 0
            if s_len==1:
                return min(counter_0, counter_1)
            s_len -= 1
        for idx in range(0, s_len, 2):
            counter_1 += 1 if (int(s[idx])+ one)==1 else 0
            counter_1 += 1 if (int(s[idx+1])+ zero)==1 else 0
            counter_0 += 1 if (int(s[idx])+ zero)==1 else 0
            counter_0 += 1 if (int(s[idx+1])+ one)==1 else 0

        return min(counter_0, counter_1)

class BestSolution:
    def minOperations(self, s: str) -> int:
        diff = 0

        for i in range(len(s)):
            if s[i] != ("1" if i % 2 == 0 else '0'):
                diff += 1

        return min(diff, len(s) - diff)