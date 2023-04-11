class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=min(prices)
        indx=prices.index(mn)
        lst=[]
        for i in range(indx,len(prices)):
            lst.append(prices[i])
        mx=max(lst)    
        profit_max=mx-mn
        return profit_max

            
