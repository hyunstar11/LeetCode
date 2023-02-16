class Solution:
    def romanToInt(self, s: str) -> int:
        # 7개 알파벳에 대해 신언
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  
        
        # 계산된 값을 위한 변수를 선언 
        result = 0 
        
        # 입력된 값의 길이만큼 for loop 을 실행
        for i in range(len(s)):

        # 만약 i 가 0 보다 큼 &   
            if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:  # 뒤에 오는 알파벳이 앞에 오는 알파벳보다 더 크면? 
                result += roman_map[s[i]] - 2 * roman_map[s[i - 1]] #  뒤에 오는 알파벳 - 앞에오는 알파벳 * 2 
            else:
                result += roman_map[s[i]] # 처음 시작할 때는 웬만하면 여기를 거침.. + 1 , 혹은 III 같은 로만넘버가 입력 될 때도 해당됨
        return result
