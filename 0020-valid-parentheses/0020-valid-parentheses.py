class Solution:
    def isValid(self, s: str) -> bool: # 스트링 값을 인풋 받고, 인풋 스트링이 parentheses, bracket, brace 인지에 대한 불리언 값을 리턴함
        stack = [] # 빈 스택을 선언함 
        for p in s: # for loop 선언 
            if p == "(" or p == "[" or p == "{": # 각 캐릭터 p 에 대해, p가 opening bracket 인지 확인한다 
                stack.append(p) # 맞으면 stack에 넣어줌 
            elif p == ")" and stack and stack[-1] == "(": # opening bracket이 아니라 closing인지, 스택에 들은 게 있는지, 그리고 스택에 opening bracket이 있는지 확인
                stack.pop() # 맞다면 opening bracket을 제거한다 
            elif p == "]" and stack and stack[-1] == "[": # same 
                stack.pop() # same 
            elif p == "}" and stack and stack[-1] == "{":
                stack.pop()# same 
            else:
                return False # 만약에 해당사항이 없다면 거짓을 return 
        return len(stack) == 0 # stack을 모두 제거했을 때 aka bracket들이 모두 매치가 될 때, bracket을 제거하면 길이가 0 이 되니까 참 값을 return 
 
