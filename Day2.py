###Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        track = set()
        for i in arr:
            if i*2 in track:
                return True
            if i%2 == 0 and int(i/2) in track:
                return False
            track.add(i)
            
# using hashmap
# O(n)
