class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        n = len(s)
        zigzag = []
        ptr = 0
        mode = numRows - 1
        while ptr < n:
            row = []
            # mode = mode % (numRows - 1) if numRows > 1 else 0
            if numRows - 1 < 1:
                row.append(s[ptr])
                ptr += 1
            elif mode % (numRows - 1) == 0:
                for _ in range(numRows):
                    row.append(s[ptr] if ptr < n else '')
                    ptr += 1
            else:
                for i in range(numRows):
                    if i == mode:
                        row.append(s[ptr])
                        ptr += 1
                    else:
                        row.append('')
            mode = mode - 1 if mode - 1 > 0 else numRows - 1
                
            zigzag.append(row)
        

        zigzag_t = []
        for _ in range(numRows):
            zigzag_t.append([''] * len(zigzag))
        
        for i in range(len(zigzag)):
            for j in range(len(zigzag[i])):
                zigzag_t[j][i] = zigzag[i][j]
        
        # print(zigzag_t)
        ans = ''
        for i in range(len(zigzag_t)):
            ans += "".join(zigzag_t[i])
        return ans

# P     I    N
# A   L S  I G
# Y A   H R   
# P     I     



s = Solution()
# print(s.convert("PAYPALISHIRING", 3))
# print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
# print(s.convert("A", 1))