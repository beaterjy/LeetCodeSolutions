class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        非递归实现
        定义opt[r][x]，长度为r，最后一个元素为x的数量
        '''
        opt = [ [0 for r in range(5)] for c in range(n) ] 
        a, e, i, o, u = [0, 1, 2, 3, 4]
        kmod = 10 ** 9 + 7
        
        #0st row set 1
        for j in  range(5):
            opt[0][j] = 1
        
        for r in range(1, n):
            #back x=a 
            opt[r][a] = (opt[r-1][e] + opt[r-1][i] + opt[r-1][u]) % kmod
            #back x=e
            opt[r][e] = (opt[r-1][a] + opt[r-1][i]) % kmod
            #back x=i
            opt[r][i] = (opt[r-1][e] + opt[r-1][o]) % kmod
            #back x=o
            opt[r][o] = (opt[r-1][i])
            #back x=u
            opt[r][u] = (opt[r-1][i] + opt[r-1][o]) % kmod
            
        return sum(opt[n-1][:]) % kmod
    
    
            
        