# Missing Number Leetcode question
class Solution(object):
    def missingNumber(self, nums):
        add=0
        add1=0
        for i in range(len(nums)+1):
            add+=i
        for i in nums:
            add1+=i
        return add-add1