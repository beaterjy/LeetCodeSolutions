class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''最长公共前缀'''
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        lens = [len(s) for s in strs]
        length = min(lens)
        temp = strs[lens.index(length)]

        i, ok = 0, True
        for i in range(length):
            for s in strs:
                if temp[:i+1] != s[:i+1]:
                    ok = False
                    break
            if not ok:
                break

        return temp[:i+1] if ok else temp[:i]
