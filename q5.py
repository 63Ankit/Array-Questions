# AJP for below requirements:
# Original Array=[2,5,4,3,6]
# Resultant Array=[360,144,180,240,120]

class Solution:
    def final(self,nums):
        arr=[]
        for i in range(len(nums)):
            add=1
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    continue
                else:
                    add=add*nums[j]
            arr.append(add)
        return arr
            
ob1=Solution() 
Array=[2,5,4,3,6]
print(ob1.final(Array))