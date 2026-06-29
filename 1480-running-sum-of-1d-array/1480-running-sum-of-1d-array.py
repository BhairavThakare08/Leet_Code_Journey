class Solution(object):
    def runningSum(self, nums):
        runningsum = []
        total = 0
        for num in nums:
            total += num
            runningsum.append(total)
        return runningsum    