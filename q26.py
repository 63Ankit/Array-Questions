#WAJP to check if an array is strictly increasing. 
'''
i/p=[2, 3, 7, 8, 9]
o/p= Array is strictly increasing

'''
class Solution:
    def incresed_array(self,nums):
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                continue
            else:
                return "Array is not strictly increasing"
        return "Array is strictly increasing"



ob1=Solution()
Input=[2, 3, 7, 8, 9]
print(ob1.incresed_array(Input))