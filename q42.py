#  WAJP to print Smallest and second Smallest element of the array.
'''
 a=[80, 80, 43, 50, 38, 63, 58, 80]
 o/p=
 38
 43
 '''
class Solution:
    def Smallest_and_Secound_Smallest(self,nums):
        Smallest=nums[i]
        Secound_Smallest=nums[i]
        for i in range(len(nums)):
            if nums[i]<Smallest:
                Smallest=nums[i]
            if nums[i]<Secound_Smallest and nums[i]>Biggest:
                Secound_Smallest=nums[i]
        return Smallest ,Secound_Smallest

ob1=Solution()
a=[80, 80, 43, 50, 38, 63, 58, 80]
a1,a2=ob1.Smallest_and_Smallest_Biggest(a)
print(a1,a2)