class Solution:
    def isValid(self, s: str) -> bool:
        p1 = {"(": 0, ")": 0}
        p2 = {"{": 0, "}": 0}
        p3 = {"[": 0, "]": 0}

        for _s in s:
            if _s == "(" or _s == ")":
                p1[_s] = p1.get(_s) + 1
            elif _s == "{" or _s == "}":
                p2[_s] = p2.get(_s) + 1
            elif _s == "[" or _s == "]":
                p3[_s] = p3.get(_s) + 1
        return p1.get("(") == p1.get(")") and p2.get("{") == p2.get("}") and p3.get("[") == p3.get("]")
  
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([])"))
    print(s.isValid("([)]"))