#  Q:28 WAJP to move all zeroes of an array to the end.
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
Input=[7, 0, 2, 6, 0, 4]
Output=[7, 2, 6, 4, 0, 0]

'''
class Solution:
    def Swift_Zero_at_end(self,nums):
        
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                if i!=j:
                    nums[j]=0
                i+=1

        return nums
        




ob1=Solution()
nums=[7, 0, 2, 6, 0, 4]
print(ob1.Swift_Zero_at_end(nums))

