class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        table = set()
        longest = 0

        while end < len(s):
            if s[end] not in table:
                table.add(s[end])
                longest = max(longest, end-start+1)
                end +=1

            else:
                table.remove(s[start])
                start+=1

        return longest