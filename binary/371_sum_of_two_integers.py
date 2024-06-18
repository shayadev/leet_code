"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
"""


class Solution:
    def getSum(self, a: int, b: int):
        shortner = 0xffffffff

        while (b & shortner) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & shortner) if b > 0 else a
