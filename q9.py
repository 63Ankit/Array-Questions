# Max consecutive n in any array
'''
array=[0,1,1,1,2,2,1,1,1,1,0]
Enter the number which max consecutive you want: 2
2
'''
class Solution:
    def Max_Consecutive(self,nums):
        count1=0
        count2=0
        n=int(input("Enter the number which max consecutive you want: "))
        for i in range(len(nums)+1):
            if i!=len(nums) and nums[i]==n:
                count2+=1
            else:
                if count2>count1:
                    count1=count2
                count2=0 
        return count1

ob1=Solution()
array=[0,1,1,1,2,2,1,1,1,1,0]
print(ob1.Max_Consecutive(array))




