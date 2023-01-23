class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_list = list()
        sum_list.append(nums[0])

        for i in range(1, len(nums)):
            sum_list.append(sum_list[i - 1] + nums[i])

        return sum_list