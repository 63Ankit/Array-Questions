# 
class Solution(object):
    def runningSum(self, nums):
        nums1=[]
        for i in range(1,len(nums)+1):
            add=0
            j=0
            while(j<i):
                add=add+nums[j]
                j+=1
            nums1.append(add)
        return nums1
    
    #--------------------------------------------------------
    