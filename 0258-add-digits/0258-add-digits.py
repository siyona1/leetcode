class Solution(object):
    def addDigits(self, n):
        sum = 0
        while n:
            sum += int(n % 10)
            n = int(n / 10)
            if n == 0 and sum < 10:
                return sum
            elif n == 0 and sum >= 10:
                n = sum
                sum = 0
        return 0
        