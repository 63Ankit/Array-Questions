# For the given array of Strings, print and count all the Strings which has even number of characters.
# Array=["Ankit","Ravi","Python","Volume","Docker"]
'''
Ravi
Python
Volume
Docker
4
'''
class Solution:
    def count(self,nums):
        count=0
        for i in nums:
            if len(i)%2==0:
                print(i)
                count+=1
        return count
ob1=Solution()
Array=["Ankit","Ravi","Python","Volume","Docker"]
count=ob1.count(Array)
print(count)

