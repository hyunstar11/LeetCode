class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = [0] * len(accounts)
        for i in range(0, len(accounts)):  
            su = sum(accounts[i])
            sums.append(su)
        return max(sums)  #test