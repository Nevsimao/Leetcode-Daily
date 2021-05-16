# 

## 

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
