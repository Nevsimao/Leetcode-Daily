# Increasing Triplet Subsequence

## Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

### Solution (Python)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sNum = s_Num = sys.maxsize
        for num in nums:
            if num <= sNum:
                sNum = num
            elif num <= s_Num:
                s_Num = num
            else:
                return True
            
        return False
