"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

"""


class Solution(object):
    def productExceptSelf(self, nums):
        product_nums = []
        cur_product = 1
        for n in nums:
            cur_product *= n
            product_nums.append(cur_product)

        reverse_product_nums = [0 for i in range(len(nums))]
        cur_product = 1
        for i in range(len(nums) -1, -1, -1):
            cur_product *= nums[i]
            reverse_product_nums[i] = cur_product

        result = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if i - 1 < 0:
                before = 1
            else:
                before = product_nums[i - 1]

            try:
                after = reverse_product_nums[i + 1]
            except IndexError:
                after = 1

            result[i] = before * after

        return result



def main():
    Solution().productExceptSelf([1, 2, 3, 4])


if __name__ == '__main__':
    main()
