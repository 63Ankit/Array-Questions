#
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count1=0
        count2=0
        for i in range(len(nums)+1):
            
            if i!=len(nums) and nums[i]==1:
                count2+=1
            else:
                if count2>count1:
                    count1=count2
                count2=0
        return count1









