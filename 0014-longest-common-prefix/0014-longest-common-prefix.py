class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         # If the array is empty, return an empty string
        if not strs:
            return ""

        # Find the shortest string in the array
        shortest_str = min(strs, key=len)

        # Loop through the characters in the shortest string
        for i, char in enumerate(shortest_str):
            # Check if the character matches the corresponding character in each string
            for string in strs:
                if string[i] != char:
                    # If there is no match, return the prefix up to this point
                    return shortest_str[:i]

        # If all strings match up to the length of the shortest string, return the shortest string
        return shortest_str