"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""


class Solution:
    def countBits(self, n: int):
        num_list = []
        for i in range(0, n + 1):
            num_list.append(i)

        output = []
        for n in num_list:
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2

            counter = 0
            for i in binary:
                if i == '1':
                    counter += 1
            output.append(counter)
        return output


if __name__ == '__main__':
    n = 5
    print(Solution().countBits(n))


"""
better solution:
class Solution:
    def countBits(self, n: int):
        dp=[0]*(n*1)
        offset=1
        for i in range(1,n+1)
            if offset * 2 ==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return dp
        
"""
