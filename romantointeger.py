class Solution(object):
    def romanToInt(self, s):
        romandict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        numerals = [numeral for numeral in s]
        i = 0
        while i < len(numerals):
            if i < len(numerals) - 1 and (numerals[i] + numerals[i + 1]) in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                sum += romandict[numerals[i + 1]] - romandict[numerals[i]] 
                i += 2 
            else:
                sum += romandict[numerals[i]]
                i += 1 

        return sum
