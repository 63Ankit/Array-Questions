#  WAJP to print true if all the elements in two arrays are same otherwise print false.
'''

Input1=[10,20,30,40,50,60,70]
Input2=[10,20,30,40,50,60,70]


'''
class Solution:
    def Check_each_element(self,nums1,nums2):
        if len(nums1)!=len(nums2):
            return False
        for i in range(len(nums1)):
            if nums1[i]!=nums2[i]:
                return False
        return True

ob1=Solution()
Input1=[10,20,30,40,50,60,70]
Input2=[10,20,30,40,50,60,70]
print(ob1.Check_each_element(Input1,Input2))
