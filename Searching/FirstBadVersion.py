'''
Docstring for Searching.FirstBadVersion
Given n versions [1, 2, ..., n] and an API isBadVersion(version)
 which returns whether version is bad. You need to find the first bad version,
  which causes all the following ones to be bad. You should minimize the number of calls to the API.
  
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        while start<=n:
            mid= (start+n)/2
            if isBadVersion(mid):
                n= mid-1
            else:
                start = mid +1
        return start

            
        