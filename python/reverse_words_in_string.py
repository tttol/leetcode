class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        i = 0
        while i < len(s):
            word = ""
            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1
            
            if word == "":
                i += 1
            else:
                words.append(word)
        return " ".join(words[::-1])

s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))