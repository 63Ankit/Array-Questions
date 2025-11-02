#  Q:10  WAPP to  swap two index values of the array.
''' Input=[10,20,30,40,50,60,70]
    Output=[10,60,30,40,50,20,70]
'''
class Solution:
    def Swap_Value_inside_array(self,nums):
        n1=int(input("Enter the number which are swap: "))
        n2=int(input("Enter the number which are swap: "))
        temp=0
        i1=0
        for i in range(len(nums)):
            if nums[i]==n1:
                temp=nums[i]
                i1=i
            if nums[i]==n2:
                nums[i1]=n2
                nums[i]=temp
        return nums
ob1=Solution()
Input=[10,20,30,40,50,60,70]
print(ob1.Swap_Value_inside_array(Input))


