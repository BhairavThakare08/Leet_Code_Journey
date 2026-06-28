class Solution(object):
    def concatWithReverse(self, nums):
        ans = nums[:]
        for i in range(len(nums) - 1, -1, -1):
            ans.append(nums[i])

        return ans
        