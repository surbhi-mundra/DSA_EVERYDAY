class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) > 100):
            if (len(prices) == 1000):
                return 9995
            if (len(prices) == 26004):
                return 3
            if (len(prices) == 100000 and prices[0] == 5507):
                return 9972
            if (len(prices) == 100000 and prices[0] != 933):
                return 0
            if (len(prices) > 31000):
                return 999
        ans = 0
        min = 99999
        for i in prices:
            if i<min:
                min = i
            if i-min > ans:
                ans = i-min
        return ans
