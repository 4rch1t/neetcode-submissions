class Solution:
    def isPalindrome(self, s: str) -> bool:
        sex = ""
        for i in s:
            if i.isalnum():
                sex += i.lower()
        if sex == sex[::-1]:
            return True
        else:
            return False

        