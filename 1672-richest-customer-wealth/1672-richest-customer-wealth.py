class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = [0] * len(accounts) # account 길이만큼으로 생성 
        for i in range(0, len(accounts)):  # account의 길이 만큼 반복 
            su = sum(accounts[i]) # 각 어카운트의 합을 구함
            sums.append(su) # 각 합을 sums 에 추가해줌
        return max(sums)  # sums 에 있는 것 중 가장 큰 값을 찾기 