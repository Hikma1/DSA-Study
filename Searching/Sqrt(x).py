'''
69. Sqrt(x) :
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''
'''here is the logical approach to solve the problem:
1. Initialize two pointers, left and right, to 0 and x respectively.
2. While left is less than or equal to right:
    a. Calculate the mid-point between left and right.
    b. If mid * mid is equal to x, return mid.
    c. If mid * mid is less than x, move the left pointer to mid + 1.
    d. If mid * mid is greater than x, move the right pointer to mid - 1.
3. If the loop ends, return right as the integer square root of x.  
    '''
class Solution(object):
    def mySqrt(self, x):
        start = 0
        end = x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        return end
# Example usage:
solution = Solution()
print(solution.mySqrt(81))  # Output: 2