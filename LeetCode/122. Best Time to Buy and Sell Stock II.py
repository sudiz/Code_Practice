class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices=prices[::-1]
        res=0
        for i in range(0,len(prices)-1):
            if prices[i]-prices[i+1]>0:
                res+=prices[i]-prices[i+1]
        return res
