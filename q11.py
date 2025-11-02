#  WAJP to reverse each element of the array.
''' Input=[10,20,30,40,50,60,70]
    Output=[70,60,50,40,30,20,10]
'''
class Solution:
    def swap_element_of_array(self,nums):
        start=0
        end=len(nums)-1
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        return nums
ob1=Solution()
Input=[10,20,30,40,50,60,70]
print(ob1.swap_element_of_array(Input))

