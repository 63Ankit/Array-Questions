#  Q:22 = WAPP to rotate all the elements of array k position to its left.

'''
Input= [1,2,3,4,5,6,7] 
k=1
Output: [2, 3, 4, 5,6,7,1]

'''
class Solution:
    def reverse(self,start,end,nums):
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        return nums
    def left_Rotate(self,position,nums):
        self.reverse(0,len(nums)-1,nums)
        
        self.reverse(0,len(nums)-position-1,nums)
        self.reverse(len(nums)-position,len(nums)-1,nums)
        return nums
ob1=Solution()
Input= [1,2,3,4,5,6,7]
k=int(input("Enter the kth position for rotation: "))
print(ob1.left_Rotate(k,Input))