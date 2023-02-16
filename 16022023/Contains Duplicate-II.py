# Question 219: Contains Duplicate-II : https://leetcode.com/problems/contains-duplicate-ii/description/

# Approach:
"""

"""


# My Solution:(Brute Force)
def mySolution(nums,k):
    for i in range(len(nums)-1):
        if i+k<len(nums):
            if nums[i] in nums[i+1:i+k]:
                return True
        else:
            if nums[i] in nums[i+1:len(nums)]:
                return True


def mySolution2(nums,k):
    for i in range(len(nums) - 1):
        j=i+1
        while(abs(i-j)<=k):
            if nums[i]==nums[j]:
                return True
            if j<len(nums):
                j+=1


# Error(if any):
"""
TLE
"""

# Optimized Solution:
def myOptimizedSolution(nums,k):
    pass


# Original Solution:
def originalSolution(nums,k):
    pass


# Mistake(Difference):
""""""

# Note/Concept:
""""""

# Solution Execution:
if __name__ == '__main__':

    nums1 = [1,2,3,1]
    k1 = 3
    nums2 = [1,2,3,1,2,3]
    k2 = 1

    print(f"My first solution: {mySolution(nums1,k1)}")
    print(f"My second solution: {mySolution2(nums1,k1)}")
    print(f"My optimized solution: {myOptimizedSolution(nums1,k1)}")
    print(f"Original solution: {originalSolution(nums1,k1)}")