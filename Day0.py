# 3Sum

## Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

### Solution (Python)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return a list of list
        # sort the imput array
        # using each num as aposible fist value
        # if not the fist value and value the same as the preios we want to continue
        # a two pointer solution to solve twoSum
        # left and right can't be equal
        # if greater then zero we have to decrease it
        # if too small we need to increase it
        # if equal to zero we add to results
        # update pointer
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            flag, left, right = nums[i]*-1, i + 1, N - 1
            while left < right:
                if nums[left] + nums[right] == flag:
                    result.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                elif nums[left] + nums[right] < flag:
                    left = left + 1
                else:
                    right = right - 1
                        
        return result
