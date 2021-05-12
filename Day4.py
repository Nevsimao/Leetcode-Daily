### Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

## Notice that the solution set must not contain duplicate triplets.

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
        
        result = []
        nums.sort() # o(nLog)
        
        for i, x in enumerate(nums): # o(n2)
            if i > 0 and x == nums[i - 1]: 
                continue 
                
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = x + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([x, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and 1 < right:
                        left += 1
                        
        return result # o(n2)
