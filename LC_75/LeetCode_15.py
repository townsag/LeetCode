def main():
    nums = [-1, 0, 1, 2, -1, -4]
    temp = Solution()
    print(temp.threeSum(nums))


# Notice that the solution set must not contain duplicate triplets.
# The order of the triplets doesnt matter, ex: [1, 0, -1] == [1, -1, 0]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited_values = set()
        sums = list()

        # start with brute force solution
        # start with unsorted array and sort the array
        sorted_nums = sorted(nums)
        for index in range(len(sorted_nums)):
            print(f"\nindex: {index}, value at index: {sorted_nums[index]}")
            print("visited values: ", visited_values)
            if sorted_nums[index] in visited_values:
                continue
            visited_values.add(sorted_nums[index])
            print(f"adding {sorted_nums[index]} to visited values")
            # treat all the numbers after index as sub array
            # iterate through the sub array to find the two indexes which sum to the target
            target = 0 - sorted_nums[index]
            high = len(sorted_nums) - 1
            low = index + 1
            low_visited_values = set()
            print(f"current index: {index}")
            print(f"starting index for low and high: {low}, {high}")
            # print(f"values at low and high: {sorted_nums[low]}, {sorted_nums[high]}")
            print(f"sorted nums: ", sorted_nums)
            while high > low:
                if sorted_nums[high] + sorted_nums[low] == target:
                    if sorted_nums[low] not in low_visited_values:
                        low_visited_values.add(sorted_nums[low])
                        print("adding to sums: ", [sorted_nums[index], sorted_nums[low], sorted_nums[high]])
                        sums.append([sorted_nums[index], sorted_nums[low], sorted_nums[high]])
                    else:
                        low += 1
                elif sorted_nums[high] + sorted_nums[low] < target:
                    low += 1
                else:
                    high -= 1
        return sums


if __name__ == "__main__":
    main()
