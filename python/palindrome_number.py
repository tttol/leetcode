class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        reversed_str_x = "".join(list(reversed(list(str_x))))

        return str_x == reversed_str_x
        