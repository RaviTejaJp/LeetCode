class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        else:
            result = 1
            max_possible = len(set(s))
            
            for i in range(max_possible,1,-1):
                substr_len = i
                start_index = 0
                while start_index <= len(s)-i:
                    substr = s[start_index:start_index+i]
                    start_index = start_index+1
                    if len(set(substr)) == len(substr) and len(substr) > result:
                        result = len(substr)
                        return result
            return result
