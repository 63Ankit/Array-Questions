#  WAJP to check whether a given array is in sorted order or not.
'''
Input=[2, 7, 7, 8, 9]
Output= Array is sorted
'''
class Solution:
    def incresed_array(self,nums):
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            else:
                return "Array is not sorted"
        return "Array is sorted"

ob1=Solution()
Input=[2, 7, 7, 8, 9]
print(ob1.incresed_array(Input))