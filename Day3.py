# Longest Substring Without Repeating Characters

## Given a string s, find the length of the longest substring without repeating characters.

### Solution (Python)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right, left, s_len = {}, 0, 0
        for i in range(0, len(s)):
            # get the last index s[i]
            # update the right index
            # get maximum of last and right
            # at that index add 1
            if s[i] in right:
                left = max(left, right[s[i]] + 1)
            # update the result
            s_len = max(s_len, i - left + 1)
            # update right index
            right[s[i]] = i
        return s_len
