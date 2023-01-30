def main():
    numbers = [1, 2, 3, 4, 4, 9, 56, 90]
    target = 8
    temp = Solution()
    print(temp.twoSum(numbers, target))


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # iterate through the list, looking at each number and then searching for the number that would make it sum to
        # the target number
        # for index in range(len(numbers)):
        #     look_for = target - numbers[index]
        #     print(f"index: {index}, {numbers[index]}, look_for: {look_for}")
        #     # only need to look at the indexes coming after the current index
        #     search_index = self.binary_search(numbers, index + 1, len(numbers) - 1, look_for)
        #     print(search_index)
        #     if search_index != -1:
        #         if index is not search_index:
        #             return [index + 1, search_index + 1]

        # try and write the two pointers solution, might be more optimal than the binary search solution
        high = len(numbers) - 1
        low = 0
        # iteratively increase the low pointer or decrease the high pointer looking for the two indexes corresponding
        # to the numbers which cum to the target
        # increase the low index if the sum of the two numbers pointed to by the low and high pointer is less than
        # the target, decrease the high index if the sum is too big
        while high > low:
            if numbers[high] + numbers[low] == target:
                return [low + 1, high + 1]
            if numbers[high] + numbers[low] < target:
                low += 1
            else:
                high -= 1

    def binary_search(self, numbers, low, high, look_for):
        # base case, array of size one can be checked for containing look for in constant time
        if high < low:
            return -1
        else:
            middle = low + (high - low) // 2
            if numbers[middle] == look_for:
                return middle
            elif numbers[middle] < look_for:
                return self.binary_search(numbers, middle + 1, high, look_for)
            else:
                return self.binary_search(numbers, low, middle - 1, look_for)


if __name__ == "__main__":
    main()
