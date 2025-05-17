class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        planted = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                planted += 1
            return planted >= n
        
        for i in range(0, len(flowerbed)):
            if i == 0:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    planted += 1
                    continue
            
            if i == len(flowerbed) - 1:
                if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                    flowerbed[-1] = 1
                    planted += 1
                    continue
                           
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                planted += 1
        
        return planted >= n
    
s = Solution()
print(s.canPlaceFlowers([0], 1))
print(s.canPlaceFlowers([1], 0))
print(s.canPlaceFlowers([1], 1))
print(s.canPlaceFlowers([1,0,0,0,1], 1))
print(s.canPlaceFlowers([1,0,0,0,1], 2))