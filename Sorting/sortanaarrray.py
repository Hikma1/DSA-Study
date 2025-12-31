'''
Docstring for Sorting.sortanaarrray
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
'''
'''
logic for this problem:we can use the bubble sort algorithm to sort the array in ascending order.
We will iterate through the array multiple times, and in each iteration, we will compare adjacent elements
and swap them if they are in the wrong order. This process will continue until the entire array is sorted.
'''
class Solution(object):
    def sortArray(self, nums):
       n= len(nums)
       for i in range(n):
        for j in range(0, n-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1]=nums[j+1],nums[j]
       return nums