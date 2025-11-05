# Q:23 WAPP find missing element from a given array which has a missing element in a range of n.
'''
 N=7
 Input: [7, 4,3, 2, 5, 1, 6]
 o/p: 2
 '''
class Solution:
    def Missing_number(self,N,nums):
        add=0
        add1=0
        for i in range(N+1):
            add+=i
        for i in nums:
            add1+=i
        return add-add1
ob1=Solution()
Input=[7, 4,3, 2, 5, 1, 6] 
N=7
print(ob1.Missing_number(N,Input))
    





