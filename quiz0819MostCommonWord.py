class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #用字典来存储单词和次数，并且维护一个最佳答案
        
        d = {}
        #标记禁用列表
        for x in banned:
            d[x] = -1
        
        #字段转化成小写
        content = paragraph.lower()
        pattern = string.punctuation
        for c in string.punctuation:
            content = content.replace(c, ' ')
        words = content.split()
        maxn = 0
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                if d[word] != -1:
                    d[word] += 1
            if d[word] > maxn:
                maxn = d[word]
                ans_str = word
        return ans_str
