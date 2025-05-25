class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(char):
            return char == "a" or char == "e" or char =="i" or char == "o" or char == "u"
        
        vowels_count = 0
        for char in s[:k]:
            if is_vowel(char):
                vowels_count += 1
        
        current_vowels_count = vowels_count
        n = len(s)
        for i in range(k, n):
            if is_vowel(s[i - k]):
                current_vowels_count -= 1
            if is_vowel(s[i]):
                current_vowels_count += 1
            vowels_count = max(vowels_count, current_vowels_count)
        return vowels_count
    
s = Solution()
print(s.maxVowels(s = "abciiidef", k = 3))
print(s.maxVowels(s = "aeiou", k = 2))
print(s.maxVowels(s = "leetcode", k = 3))