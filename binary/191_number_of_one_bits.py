"""
Write a function that takes the binary representation of a positive integer and returns the number of
set bits
it has (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:

The input binary string 1011 has a total of three set bits.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        if n == 0:
            return 0
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n = n // 2

        for i in binary:
            if i == '1':
                counter += 1
        return counter


if __name__ == '__main__':
    n = 13
    print(Solution().hammingWeight(n))
