class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFrequency = {}
        tFrequency = {}
        for i in s:
            if i in sFrequency:
                sFrequency[i] +=1
            else:
                sFrequency[i] = 1

        for i in t:
            if i in tFrequency:
                tFrequency[i] +=1
            else:
                tFrequency[i] = 1

        return sFrequency == tFrequency


        