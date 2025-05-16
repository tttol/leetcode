class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        i1, i2 = 0, 0
        for i in range(len(word1) + len(word2)):
            if i%2 == 0:
                ans += word1[i1]
                i1 += 1
            else:
                ans += word2[i2]
                i2 += 1
            
            if i1 >= len(word1):
                ans += word2[i2:]
                break
            elif i2 >= len(word2):
                ans += word1[i1:]
                break
        
        return ans

s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))
print(s.mergeAlternately("abcd", "pq"))