class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        '''分糖果2'''
        ans = [0] * num_people
        i = 0
        while candies > 0:
            candy = i + 1
            if candy <= candies:
                candies -= candy
                ans[i % num_people] += candy
            else:
                ans[i % num_people] += candies
                break
            i += 1
        return ans
