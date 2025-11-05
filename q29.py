# Q:29 WAJP the shift all 0’s to left and all 1’s to the right(Without Sorting).
# Given an integer array nums, move all 0's to the start of it while maintaining the relative order of the non-zero elements.
'''
 Input=[0, 1, 1, 0, 0, 1, 0, 0]
 Output=[0, 0, 0, 0, 0, 1, 1, 1]

 '''
class Solution:
    def Swift_zero_left_side(self,nums):
        '''
        # maintaining the relative order of the non-zero elements si not followed in this code. 
        start=0
        end=len(nums)-1
        while start<end:
            if nums[start]!=0:
                nums[end]=nums[start]
                nums[start]=0

                end-=1
            start+=1
        return nums
        '''
        
ob1=Solution()
Input=[0, 1, 1, 0, 0, 1, 0, 0]
print(ob1.Swift_zero_left_side(Input))





