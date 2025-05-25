class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for _s in s:
            if _s == "*" and ans != []:
                ans.pop()
            elif _s != "*":
                ans.append(_s)
        return "".join(ans)
    
s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
print(s.removeStars("*a"))