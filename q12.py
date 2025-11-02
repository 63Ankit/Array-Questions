# WAJP to reverse 1st half and 2nd half elements of array.
''' Input=[10,20,30,40,50,60,70]
    Output=[40,30,20,10,70,60,50]
'''
class Solution:
    def reverse_Array(self,start,end,nums):
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            return nums
    def Calling(self,nums):
        mid=len((nums))//2
        nums1=self.reverse_Array(0,mid,nums)
        nums1=self.reverse_Array(mid+1,len(nums)-1,nums)
        return nums1
ob1=Solution() 
Input=[10,20,30,40,50,60,70]
print(ob1.Calling(Input))


