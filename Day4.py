#   Longest Palindromic Substring

## Given a string s, return the longest palindromic substring in s

### Solution (Python)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        resultLen = 0
        
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resultLen:
                    result = s[left: right + 1]
                    resultLen = right - left + 1
                left -= 1
                right += 1
                
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resultLen:
                    result = s[left: right + 1]
                    resultLen = right - left + 1
                left -= 1
                right += 1
        return result
