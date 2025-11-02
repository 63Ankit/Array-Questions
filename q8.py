# Max consecutive 1 in any array.
'''
array=[0,1,1,1,2,2,1,1,1,1,0]
output=4
'''
class Solution:
    def Max_Consecutive(self,nums):
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

ob1=Solution()
array=[0,1,1,1,2,2,1,1,1,1,0]
print(ob1.Max_Consecutive(array))