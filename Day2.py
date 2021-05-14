# Group Anagrams

## Given an array of strings strs, group the anagrams together. You can return the answer in any order.

### Solution (Python)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} #using a dic to comper using keys
        for i in strs:
            key = ''.join(sorted(list(i))) #sort it, conver to a list and then join it back to string format
            if key in result:
                result[key].append(i) #if sorted strigs are the same it can be append them to the dic
            else:
                result[key] = [i]
        return result.values()
