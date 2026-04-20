class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFrequency = {}
        tFrequency = {}
        
        for c in s:
            sFrequency[c] = sFrequency.get(c,0) + 1

        for c in t:
            tFrequency[c] = tFrequency.get(c,0) + 1

        return sFrequency == tFrequency

        