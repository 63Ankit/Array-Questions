# WAJP to insert an element at certain position of the array.
'''
Input=[10,20,30,40,50]
Output=[10,20,25,30,40,50]
'''
class Solution:
    def insertAtIndex(self, nums, index, value):
        # Edge case: invalid index
        if index < 0 or index > len(nums):
            return nums  # or raise an error

        # Create a new array with space for the new element
        result = [0] * (len(nums) + 1)

        for i in range(len(nums) + 1):
            if i < index:
                result[i] = nums[i]
            elif i == index:
                result[i] = value
            else:
                result[i] = nums[i - 1]

        return result

# Example usage
sol = Solution()
nums = [10, 20, 30, 40]
index = 2
value = 99
print("Before:", nums)
print("After:", sol.insertAtIndex(nums, index, value))
        

