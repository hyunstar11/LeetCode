class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]','',s).lower()
    # s = s.replace(" ","").lower()
       # s = s.replace(':','')
       # s = s.replace('[','')
       # s = s.replace(']','')
        return s == s[::-1]
            #return f'"{s}" is a palindrome.'
        #else: 
         #   return f'"{s}" is not a palindrome.'

        