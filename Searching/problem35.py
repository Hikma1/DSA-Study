'''
Docstring for Searching.problem35
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''
'''Here is the logical approach to solve the problem:
1. Initialize two pointers, left and right, to the start and end of the array.
2. While left is less than or equal to right:
    a. Calculate the mid-point between left and right.
    b. If the element at mid is equal to the target, return mid.
    c. If the element at mid is less than the target, move the left pointer to mid + 1.
    d. If the element at mid is greater than the target, move the right pointer to mid - 1 
3. If the loop ends, return left as the insertion index for the target.
    '''
class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)-1
        while start<=end:
            mid =(start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end =mid-1
            else :
                start=mid+1
        return start
        