class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        '''二叉树寻路'''
        # TODO: i == 1
        arr, depth = [0], 0
        # generate the tree arr
        while True:
            head = 2 ** depth
            temp = [head + i for i in range(head)]
            if depth % 2:
                temp.reverse()
            arr += temp
            if label in temp:
                break
            depth += 1
        
        ans = []
        index = arr.index(label)
        while index:
            ans.append(arr[index])
            index //= 2
        
        ans.reverse()
        return ans
        
            