# WAJP to rotate all the elements of array k position to its right.
'''
Input= [1,2,3,4,5,6,7] 
k=2 
Output: [6, 7, 1, 2, 3, 4, 5]

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
    def rotate_by_k_position(self,position,nums):
        self.reverse(0,len(nums)-1,nums)
        
        self.reverse(0,position-1,nums)
        self.reverse(position,len(nums)-1,nums)
        return nums
ob1=Solution()
Input= [1,2,3,4,5,6,7] 
k=2
print(ob1.rotate_by_k_position(k,Input))

            