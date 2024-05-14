class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
                continue
            if i % 5 == 0:
                res.append("Buzz")
                continue
            if i % 3 == 0:
                res.append("Fizz")
                continue
            res.append(str(i))
        return res