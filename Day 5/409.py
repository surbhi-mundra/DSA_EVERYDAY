""" 409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only. """

#approach 1

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        length = 0
        has_odd = False

        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        for value in freq_map.values():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                has_odd = True

        if has_odd:
            length += 1

        return length

#approach 2

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        odd_count = sum(freq & 1 for freq in counts.values())
        
        return len(s) - odd_count + (1 if odd_count > 0 else 0)

#approach 3

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        length=0
        odd_found=False
        for freq in count.values():
            if freq%2==0:
                length +=freq
            else:
                length +=freq-1
                odd_found=True
        if odd_found:
            length +=1
        return length



