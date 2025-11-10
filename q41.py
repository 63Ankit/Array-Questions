#  Q:41 WAJP to print Biggest and second biggest element of the array.
'''
a=[80, 80, 43, 50, 38, 63, 58, 80]
Output=
80
63
'''
class Solution:
    def Biggest_and_Secound_Biggest(self,nums):
        Biggest=0
        Secound_Biggest=0
        for i in range(len(nums)):
            if nums[i]>Biggest:
                Biggest=nums[i]
            if nums[i]>Secound_Biggest and nums[i]<Biggest:
                Secound_Biggest=nums[i]

        return Biggest ,Secound_Biggest
ob1=Solution()
a=[80, 80, 43, 50, 38, 63, 58, 80]
a1,a2=ob1.Biggest_and_Secound_Biggest(a)
print(a1,a2)







