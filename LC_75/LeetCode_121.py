def main():
    test = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(test.maxProfit(prices))


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # minimum length of prices is 1
        # minimum value of price in prices is 0

        """
        best_tuple = (prices[0], prices[0], 0)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > best_tuple[2]:
                    best_tuple = (i, j, prices[j] - prices[i])

        return best_tuple[2]
        """

        # try writing the two pointers solution
        running_max = 0
        left_index = 0
        right_index = 0

        while right_index < len(prices):
            # check to see if right index is less than the left index
            if prices[left_index] > prices[right_index]:
                # advance the left pointer to be pointing at the new minimum
                left_index = right_index
            # check to see if the difference between the left pointer and the right pointer values is a new max
            else:
                if prices[right_index] - prices[left_index] > running_max:
                    running_max = prices[right_index] - prices[left_index]
            right_index += 1

        return running_max




if __name__ == "__main__":
    main()
