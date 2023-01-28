def main():
    nums = [2, 7, 11, 15]
    target = 9
    temp = Solution()
    print(temp.twoSum(nums, target))


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # try the brute force solution first
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # come up with a solution which is less than O(n^2) time complexity
        # use one pass solution:
        # for each value we need to find another value that would add to the first value to make the target
        # store the value we are looking for in a hash table with the value we are looking for as the key and the
        # location of the value we found previously as the value
        wish_list = dict()      # dict[number needed to get to target, index of first number]
        for index in range(len(nums)):
            if nums[index] in wish_list:
                return [wish_list[nums[index]], index]
            else:
                wish_list[target - nums[index]] = index

if __name__ == "__main__":
    main()
