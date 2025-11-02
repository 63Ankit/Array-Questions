# 
class Solution(object):
    def getConcatenation(self, nums):
        nums1=nums
        for i in range(len(nums)):
            nums1.append(nums[i])
        return nums1