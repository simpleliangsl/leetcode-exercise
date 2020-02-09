'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
'''

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        i = 0
        max_length = 0

        while i < len(s):
            if s[i] in d:
                max_length = max(len(d), max_length)
                i = d[s[i]]
                d.clear()
            else:
                d[s[i]] = i
            
            i+=1

        return max(len(d), max_length)
