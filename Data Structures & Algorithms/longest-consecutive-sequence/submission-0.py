class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)

        longest = 0
        for i in nums:
            # start sequence
            if i-1 not in s:
                seq = 1
                while i + 1 in s:
                    seq +=1
                    i+=1
                if seq > longest:
                    longest = seq

        return longest
                
                

        