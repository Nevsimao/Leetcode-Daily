###Given an array of integers arr, return true if and only if it is a valid mountain array.

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        pointer = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if pointer == 0:
                if arr[i] > arr[i+1]: pointer = 1
            else:
                if arr[i] <= arr[i+1]:
                    return False
        return True if arr[-2] > arr[-1] and arr[0] < arr[1] else False
