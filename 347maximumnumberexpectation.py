class Solution:
    """
    @param nums: a list of positive numbers
    @return: the expectation of the maximum number
    """
    def expectMaximum(self, nums):
        # write your code here

        # dp, stack = [0], []
        # for i in range(len(nums)):
        #     while stack and nums[stack[-1]] <= nums[i]:
        #         stack.pop(-1)
        #     length = i - stack[-1] if stack else i + 1
        #     dp.append(length * nums[i] + dp[i + 1 - length])
        #     stack.append(i)
        # count = len(nums) * (len(nums) + 1) // 2
        # return sum(dp) / count