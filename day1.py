#9Palindrome Number
#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            return str(x)== str(x)[::-1]