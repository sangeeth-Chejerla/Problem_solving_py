import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        def alpha_numeric(text):

            pattern = re.compile(r"[^0-9a-zA-Z]")
            return pattern.sub("", text)
        
        answer = alpha_numeric(s).lower()

        rev = answer[::-1]

        print(rev)
        print(answer)
        return True if answer==rev else False
