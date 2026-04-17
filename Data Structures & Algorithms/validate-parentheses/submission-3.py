class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranMap = {'(': ')', '[':']', '{':'}'}

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                if paranMap[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        
        if len(stack)>0:
            return False

        return True


        