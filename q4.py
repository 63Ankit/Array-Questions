#  Q:4 WAPP for below requirements:
# Original Array=[2,5,4,3,6]
# Resultant Array=[18,15,16,17,14]
class Solution:
    add=0
    arr=[]
    def Final(self,nums):
        add=0
        arr=[] 
        for i in nums:
            add=add+i
        for i in range(len(nums)):
            nums[i]=add-nums[i]
            # Here i am work with a new array
        '''    
        for i in nums:
            add1=add
            add1=add1-i
            arr.append(add1)
        '''
        return nums
ob1=Solution()
Array=[2,5,4,3,6]
print(ob1.Final(Array))



