# 숫자 리스트 -> 스트링으로 변환 후 합침 -> 다시 바꾸고 + 1 -> 그 최종 숫자를 쪼개기? (쪼개는 과정에서 스트링으로 바꾸는 게 꼭 필요한가?)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         # 각 digit을 string 형태로 바꿔짐 
#         str_digits = [str(digit) for digit in digits]

#         # 그 각각의 string 들을 합침 
#         combined_str = ''.join(str_digits)

#         # 합쳐진 (concatenated) 스트링을 숫자로 바꾸고 + +1 
#         single_number = int(combined_str)+ 1 

#         # 숫자를 스트링으로 다시 바꾸기 
#         str_number = str(single_number)
    
#         # Convert each character in the string back to an integer and create a list of integers
#         digits = [int(char) for char in str_number]
        
#         return digits


# Better solution? 

          # Convert the integer array to a single integer
          
          # map 함수를 통해 list에 있는 모든 수를 str 으로 변환 
          # join 함수와 ''을 통해 str 들을 합쳐줌 --> 하나의 스트링이 됨 
            # join + '' 을 해주면 concatenate 한다고 보면 됨
          number = int(''.join(map(str, digits)))

          # Increment the integer by one
          incremented_number = number + 1

          # Convert the incremented integer back to an integer array
          incremented_digits = [int(char) for char in str(incremented_number)]

          return incremented_digits

    # Test the function with an example integer array
    # example_digits = [1, 2, 3, 4, 5]
    # print(increment_large_integer(example_digits))
