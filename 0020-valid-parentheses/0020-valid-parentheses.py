class Solution:
    def isValid(self, s: str) -> bool:
        lst = ["()", "{}", "[]"]
        while any(i in s for i in lst):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            
        if len(s) != 0:
            return False
        return True