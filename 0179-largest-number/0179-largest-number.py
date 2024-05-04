class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution(object):
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNumKey)
        largest_num = ''.join(nums)
        return "0" if largest_num[0] == "0" else largest_num
        