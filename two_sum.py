'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example: 
Given nums = [2, 7, 11, 15], target = 9, because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

https://leetcode-cn.com/problems/two-sum
'''

from typing import List

class Solution:
    
    # twoSum should be two_sum per Python name convenstion
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_to_indexs = {}

        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in num_to_indexs:
                return [num_to_indexs[m], i]
            else:
                num_to_indexs[n] = i