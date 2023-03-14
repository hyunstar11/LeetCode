# Key - Using the find function? 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: # 작은 단어가 큰 단어안에 존재하지 않으면 
            return -1 # -1 반환 
        else: 
            index = haystack.find(needle) # 그렇지 않을 경우에는.. 작은 단어가 큰 단어 안의 어디 (인덱스)에 있는지 find 한다 
            return index # 그 인덱스 값을 반환한다..  