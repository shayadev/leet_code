"""
Reverse bits of a given 32 bits unsigned integer.
Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.

"""


class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res


if __name__ == '__main__':
    n =43261596
    print(Solution().reverseBits(n))
