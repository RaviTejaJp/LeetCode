class Solution:
    def romanToInt(self, s: str) -> int:
        val = { "I" : 1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000}
        index = 0
        result = 0
        previous_val = 0
        while index < len(s):
            if previous_val == 0:
                result = val[s[index]]
            else:
                if previous_val < val[s[index]]:
                    result = result + val[s[index]] - 2*previous_val
                else:
                    result = result + val[s[index]]
            previous_val = val[s[index]]
            index = index + 1
            
        return result
