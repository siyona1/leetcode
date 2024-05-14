class Solution:
	def summaryRanges(self, nums):

		result = []

		start , end = 0 , 0

		while start < len(nums) and end < len(nums):

			if (end + 1) < len(nums) and nums[end] + 1 == nums[end + 1]:
				end = end + 1
			else:

				if nums[start] == nums[end]:
					result.append(str(nums[start]))
					start = start + 1
					end = end + 1

				else:
					result.append(str(nums[start]) + '->' + str(nums[end]))
					end = end + 1
					start = end

		return result
