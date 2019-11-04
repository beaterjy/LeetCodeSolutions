class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        '''
        回溯法
        '''
        ans = []
        def backtrack(s, i, n):
            if i < n:
                if s[i] >= 'a' and s[i] <= 'z': #s[i]为小写字母
                    backtrack(s, i+1, n)
                    newS = s[:i] + s[i].upper() + s[i+1:]
                    backtrack(newS, i+1, n)
                elif s[i] >= 'A' and s[i] <= 'Z': #s[i]为大写字母
                    backtrack(s, i+1, n)
                    newS = s[:i] + s[i].lower() + s[i+1:]
                    backtrack(newS, i+1, n)
                else:
                    backtrack(s, i+1, n)
            else:
                ans.append(s)
        
        backtrack(S, 0, len(S))
        return ans