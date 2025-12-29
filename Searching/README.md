Searching Algorithms - DSA Study Repository
Overview
This section of the repository focuses on Searching Algorithms, a fundamental topic in Data Structures and Algorithms (DSA). Currently, it covers two core searching techniques:

Linear Search
Binary Search (and its variants)

Each algorithm includes:

Conceptual explanation and logical analysis
Time and space complexity breakdown
Python implementations
Solutions to related LeetCode problems with detailed thought process

The goal is to build a clear, beginner-friendly yet in-depth understanding of how searching works efficiently on sorted and unsorted data.
Algorithms Covered
1. Linear Search

Concept: Sequentially check each element in the list until the target is found or the list ends.
Best for: Unsorted arrays or small datasets.
Time Complexity: O(n)
Space Complexity: O(1)

LeetCode Problems Solved:

Basic implementation and variations

2. Binary Search

Concept: Divide and conquer approach on a sorted array. Repeatedly divide the search interval in half.
Key Advantage: Reduces time complexity dramatically for large sorted datasets.
Time Complexity: O(log n)
Space Complexity: O(1) (iterative), O(log n) (recursive)

Important Variants & LeetCode Problems:



































ProblemLeetCode #Key InsightSearch in Sorted Array704. Binary SearchClassic binary searchSearch Insert Position35. Search Insert PositionReturn insertion point when target not foundFind Square Root69. Sqrt(x)Binary search on answer range (1 to x)First Bad Version*278. First Bad VersionFind leftmost occurrence using binary searchPeak Index in Mountain Array*852. Peak Index in a Mountain ArrayModified binary search for peak
*Planned or in progress
Why Binary Search is Powerful