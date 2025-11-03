# LeetCode Question: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution(object):
    def reverse(self,start,end,nums):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        return nums
    def rotate(self,nums,k):
        k=k%len(nums)
        if k==0:
            return

        self.reverse(0,len(nums)-1,nums)
        
        self.reverse(0,k-1,nums)
        self.reverse(k,len(nums)-1,nums)
        return nums