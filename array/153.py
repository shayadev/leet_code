"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explana
"""


class Solution:
    def findMin(self, nums):
        result = nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mild = (left + right) // 2
            result = min(result, nums[mild])
            if nums[mild] >= nums[left]:
                left = mild + 1
            else:
                right = mild - 1

        return result
