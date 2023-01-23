class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # niaeve solution: start by checking for each index if that index is a pivot index
        # for index in range(len(nums)):
        #     right_sum = 0
        #     left_sum = 0
        #     for strict_right in range(0, index):
        #         right_sum += nums[strict_right]
        #     for strict_left in range(index + 1, len(nums)):
        #         left_sum += nums[strict_left]

        #     if left_sum == right_sum:
        #         return index

        # return -1

        # make an array holding the running sum from the left to the right
        running_sum_left = list()
        running_sum_left.append(nums[0])
        for index in range(1, len(nums)):
            running_sum_left.append(running_sum_left[index - 1] + nums[index])

        # make an array holding the running sum from right to left
        running_sum_right = [None for x in range(len(nums))]
        running_sum_right[-1] = nums[-1]
        for index in range(len(nums) - 2, 0 - 1, -1):
            running_sum_right[index] = nums[index] + running_sum_right[index + 1]

        # at this point I can get the sum before an index by adressing the running sum left array:
        # running_sum_left[index - 1]
        # and the sum after an index by adressing the running sum right array:
        # running_sum_right[index + 1]

        # check to see if it is the first index (cannot address running sum left at [0 - 1])
        # if 0 == running_sum_right[0 + 1]:
        #     return 0

        for index in range(0, len(nums)):
            if running_sum_left[index] == running_sum_right[index]:
                return index

        # check to see if it is the last index (cannot address running sum right [len + 1])
        # if 0 == running_sum_left[len(nums) - 1 -1]:
        #     return len(nums) - 1

        return -1