from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        for a in arr:
            if a not in count_map:
                count_map[a] = 1
            else:
                count_map[a] += 1
        
        count_arr = [0] * 1001
        for v in count_map.values():
            count_arr[v] += 1
            if count_arr[v] > 1:
                return False
        return True
    
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))