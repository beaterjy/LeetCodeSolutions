class Solution:
	# 有效的括号
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        arr = []
        for c in s:
            if not arr:
                arr.append(c)
                continue
            back = arr[len(arr) - 1]
            if back == '(' and c == ')' or back == '{' and c == '}' or back == '[' and c == ']':
                arr.pop()
            else:
                arr.append(c)
        return not arr
    
    