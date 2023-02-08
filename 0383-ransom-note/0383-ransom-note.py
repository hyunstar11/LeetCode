# Hash Map / Dictionary 관련 개념 
# https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4427/ 

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
    
        # Counter 함수를 통해 ransom 과 magazine을 설정..  
        # output: Counter({'a': 2, 'b': 1})... 이런식으로 알파벳이랑 그 알파벳의 개수가 대충 뜸. 
 
        # Q. Counter 없이 그냥 st1, st2 로 한다면 어떻게 되나? 
        
        # 해시 사용하기 
        st1, st2 = Counter(ransomNote), Counter(magazine) 
        # st1, st2 = ransomNote, magazine # Why can't we do this?  

        
        # ransom note와 magazine 사이에 공통으로 존재하는 요소는 무엇인지 -> 그 공통으로 존재하는 요소를 통해 ransom note를 만들 수 있는지 확인 
        return st1 & st2 == st1
    
        # A. Hash / Counter 를 쓰는 이유: 해시 없이는 위의 & operator 를 사용할 수 없음. 고로 어떤 엘레멘트가 노트와 매거진 사이에 공통으로 존재하는지 알 수 없음
        # TypeError: unsupported operand type(s) for &: 'str' and 'str'  