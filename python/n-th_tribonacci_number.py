class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0] * 38
        t[0], t[1], t[2] = 0, 1, 1

        if n < 3:
            return t[n]

        for i in range(3, 38):
            t[i] = t[i-1] + t[i-2] + t[i-3]
        return t[n]
    
if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(4))
    print(s.tribonacci(25))
    print(s.tribonacci(37))