'''

Leetcode 1915 Number of Wonderful Substrings

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.
A substring is a contiguous sequence of characters in a string. 

Example 1:
        Input: word = "aba"
        Output: 4
        Explanation: The four wonderful substrings are underlined below:
        - "aba" -> "a"
        - "aba" -> "b"
        - "aba" -> "a"
        - "aba" -> "aba"

Example 2:
        Input: word = "aabb"
        Output: 9
        Explanation: The nine wonderful substrings are underlined below:
        - "aabb" -> "a"
        - "aabb" -> "aa"
        - "aabb" -> "aab"
        - "aabb" -> "aabb"
        - "aabb" -> "a"
        - "aabb" -> "abb"
        - "aabb" -> "b"
        - "aabb" -> "bb"
        - "aabb" -> "b"

Example 3:
        Input: word = "he"
        Output: 2
        Explanation: The two wonderful substrings are underlined below:
        - "he" -> "h"
        - "he" -> "e"

Constraints:
        1 <= word.length <= 105
        word consists of lowercase English letters from 'a' to 'j'.

'''
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        prefix = 0
        count = [0] * 1024
        count[0] = 1

        for c in word:
            # Update the prefix XOR value for the current character
            prefix ^= 1 << (ord(c) - ord('a'))
            
            # Count substrings with each character occurring even number of times
            ans += count[prefix]
            
            # Count substrings with one character occurring odd number of times
            for i in range(10):
                ans += count[prefix ^ (1 << i)]

            # Increment count for the current prefix
            count[prefix] += 1

        return ans
