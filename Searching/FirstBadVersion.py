'''
Docstring for Searching.FirstBadVersion
Given n versions [1, 2, ..., n] and an API isBadVersion(version)
 which returns whether version is bad. You need to find the first bad version,
  which causes all the following ones to be bad. You should minimize the number of calls to the API.
  
'''
'''logic:
We can use binary search to minimize the number of calls to the API.
 We start with the entire range of versions from 1 to n. 
 We calculate the mid-point of the current range and check if it is a bad version using the isBadVersion API.
 If it is a bad version, we know that the first bad version must be at mid or before mid, so we adjust our search range to the left half by setting n to mid - 1.
 If it is not a bad version, we know that the first bad version must be after mid, so we adjust our search range to the right half by setting start to mid + 1.
 '''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        while start<=n:
            mid= (start+n)/2
            if isBadVersion(mid):
                n= mid-1
            else:
                start = mid +1
        return start

            
        