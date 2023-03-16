class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = [str(digit) for digit in digits]

        # Join the strings together
        combined_str = ''.join(str_digits)

        # Convert the concatenated string back into a number
        single_number = int(combined_str)+ 1 

        # Convert the number to a string
        str_number = str(single_number)
    
        # Convert each character in the string back to an integer and create a list of integers
        digits = [int(char) for char in str_number]
        
        return digits 