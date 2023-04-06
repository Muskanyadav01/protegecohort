class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        values=[]
        for i in range(len(accounts)):
            sum=0
            for j in range(len(accounts[i])):
                sum=sum + accounts[i][j]
            values.append(sum)
        return max(values)    
