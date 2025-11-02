# For the given array of Strings, print the largest string.
# Array=["Ankit","Ritik","Shubham","Mohit","Churashiya"]
# Churashiya
class Solution:
    def Largest_String(self,nums):
        biggest=""
        for i in nums:
            if len(i)>len(biggest):
                biggest=i
        return biggest
ob1=Solution()
Array=["Ankit","Ritik","Shubham","Mohit","Churashiya"]
print(ob1.Largest_String(Array))
                




