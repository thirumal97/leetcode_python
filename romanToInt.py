class Solution:
    def romanToInt(self, s: str) -> int:
        # romanString for every i in romanString
        # the first digit, 
        # get all the symbols and instances in a dict
        # we need a sliding window of size 2 here in the string
        new_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4}
        new_dict.update({'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900})
        total_num = 0
        i = 0
        while i < len(s):
            sub_string = s[i:i+2]
            if sub_string in new_dict:
                total_num += new_dict[sub_string]
                i += 2
            else:
                total_num += new_dict[s[i]]
                i +=1
        return total_num
        

if __name__ == "__main__":
    sol = Solution()
    s = 'XVIII'
    print(sol.romanToInt(s))