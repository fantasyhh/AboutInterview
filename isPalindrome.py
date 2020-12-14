"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写
输入: "A man, a plan, a canal: Panama"
输出: true
输入: "race a car"
输出: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a =  [i for i in s.lower() if i.isalpha() or i.isdigit()]
        return(a[::1]==a[::-1])



s = Solution()
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
assert(s.isPalindrome(s1)) == True
assert(s.isPalindrome(s2)) == False