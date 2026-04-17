class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in table:
                table[sorted_i] = [i]
            else:
                table[sorted_i].append(i)
        res = []
        
        for value in table.values():
            res.append(value)
        
        return res
                

        
        