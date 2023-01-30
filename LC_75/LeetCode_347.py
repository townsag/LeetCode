def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    temp = Solution()
    print(temp.topKFrequent(nums, k))


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count the frequency of each number in the list
        ledger: dict[int, int] = dict()
        for number in nums:
            if number in ledger:
                ledger[number] += 1
            else:
                ledger[number] = 1

        # dump the contents of the dictionary as a list of tuples
        ledger_tuples: list[tuple[int, int]] = list()
        for key in ledger.keys():
            # ledger_tuples.append(tuple([key, ledger[key]]))
            ledger_tuples.append((key, ledger[key]))

        ledger_tuples = sorted(ledger_tuples, key=lambda x: x[1], reverse=True)
        ret = list()
        for i in range(k):
            ret.append(ledger_tuples[i][0])
        return ret


if __name__ == "__main__":
    main()
