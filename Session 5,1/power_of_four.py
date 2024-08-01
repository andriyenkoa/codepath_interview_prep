class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        start = 1
        while True:
            if start > n:
                return False
            elif start == n:
                return True
            start *= 4
