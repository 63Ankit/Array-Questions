# WAJP to rotate each element of an array by Given Index position in right side.

'''
Input=[10,20,30,40,50,60,70]
Output=[70,20,30,40,50,60,10]
'''
class Solution:
    def reverse(self,start,end,nums):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        return nums
    def right_rotation(self,position,nums):
        self.reverse(0,len(nums)-1,nums)
        self.reverse(0,len(nums)-1-position,nums)
        self.reverse(len(nums)-position,len(nums)-1,nums)

        return nums
ob1=Solution()
Input=[10,20,30,40,50,60,70]
print(ob1.right_rotation(6,Input))
        

