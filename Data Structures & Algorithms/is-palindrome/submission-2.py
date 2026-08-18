class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
        j = len(clean_s) - 1
        for i in range(len(clean_s)):
            if clean_s[i] != clean_s[j]:
                return False
            j -= 1
        return True