class Solution:
    # 整数反转
    def reverse(self, x: int) -> int:
        mark = -1 if x < 0 else 1
        x *= mark
        
        s = str(x)
        # 内置python没有reverse
        s = s[::-1]
        
        res = int(s)
        res *= mark
        
        return res if res >= (-(2 ** 31)) and res <= (2 ** 31 -1) else 0
    