'''
Docstring for Sorting.SortByParity
Given an array of integers nums, sort the array so that all even integers
 come before all odd integers. Return any array that satisfies this condition.
'''
'''logic for this problem:
We can solve this problem by using a two-pointer approach. We will maintain two pointers, one starting from the beginning of the array and the other from the end of the array.
 The left pointer will move rightwards until it finds an odd number, and the right pointer will move leftwards until it finds an even number.
 When both pointers find their respective numbers, we will swap them. This process continues until the left pointer is greater than or equal to the right pointer.
 '''
class Solution(object):
    def sortArrayByParity(self, nums):
       n= len(nums)
       for i in range(n):
        for j in range(0, n-i-1):
            if nums[j]%2==1 and nums[j+1]%2==0:
                nums[j], nums[j+1]=nums[j+1],nums[j]
       return nums