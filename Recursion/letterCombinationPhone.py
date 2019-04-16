class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == None or len(digits)==0:
            return result
        mappings = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.letterCombinationHelper(digits, mappings, result, 0, "")
        return result
    
    def letterCombinationHelper(self, digits, mappings, result, index, current):
        if len(current) == len(digits):
            result.append(current)
        else:
            letters = mappings[int(digits[index])]
            for letter in letters:
                self.letterCombinationHelper(digits, mappings, result , index+1, current + letter)

s = Solution()
s.letterCombinations("23")