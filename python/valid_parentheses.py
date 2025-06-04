class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for _s in s:
          if _s == "(" or _s == "{" or _s == "[":
              stack.append(_s)
          elif _s == ")" or _s == "}" or _s == "]":
              if len(stack) == 0:
                  return False
              
              open_bracket = stack.pop()
              parenthese = open_bracket + _s
              if parenthese != "()" and parenthese != "{}" and parenthese != "[]":
                  return False
      return len (stack) == 0

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([])"))
    print(s.isValid("([)]"))