class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''Count Binart Substring'''
        if not s:
            return 0
        
        # set the new end 
        s = s + '2'
        
        index, res = 0, 0
        cur_c = s[0]
        cur_count, pre_count = 0, 0
        while index < len(s):
            if s[index] != cur_c:
                res += min(pre_count, cur_count)
                pre_count, cur_count = cur_count, 1
                cur_c = s[index]
            else:
                cur_count += 1
            # Increment index
            index += 1
        return res