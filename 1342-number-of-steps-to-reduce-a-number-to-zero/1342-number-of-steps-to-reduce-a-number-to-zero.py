class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        # 횟수를 세어주는 count 변수 선언 
        count = 0 
        
        # 0 이 되기 전까지 반복해주는 게 핵심 
        while num > 0:
        # 2 로 나누어 떨어진다면 // 2 로 나누었을 때 리메인더가 0 이라면?
            if num % 2 == 0:
                num = num/2
                count = count + 1
                
        # 나누어 떨어지지 않는다면? -> 홀수일 시 
            else: 
                num = num -1 
                count = count + 1 
        return count 