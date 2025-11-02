# WAJP to remove an element from the certain position of the array.
'''
Input=[10,20,30,40,50,60,70]
Output=[10,20,30,40,60,70]
'''
class Solution:
    def remove_an_element(self,nums,index):
        
        '''
        nums1=[]
        for i in range(len(nums)):
            if i==4:
                continue
            else:
                nums1.append(nums[i])
        return nums1
        '''
        nums1=[0]*(len(nums)-1)
        for i in range(len(nums)):
            if i<index:
                nums1[i]=nums[i]
            elif i==index:
                continue
            else:
                nums1[i-1]=nums[i]
        return nums1



ob1=Solution()
Input=[10,20,30,40,50,60,70]
print(ob1.remove_an_element(Input,4))






