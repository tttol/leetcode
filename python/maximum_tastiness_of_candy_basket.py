# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/solutions/2948107/binary-search/
class Solution(object):
    def maximumTastiness(self, price, k):
        price.sort()
        def check(x):
            last, count, i = price[0], 1, 1
            while count < k and i < len(price):
                if price[i] - last >= x:
                    last, count = price[i], count + 1
                i += 1
            return count == k
        lo, hi = 0, 10 ** 9
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): lo = mid + 1
            else: hi = mid
        return lo - 1

s = Solution()
print(s.maximumTastiness([13,5,1,8,21,2], 3)) 
# print(s.maximumTastiness([1,3,1], 2)) 