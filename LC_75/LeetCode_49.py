from functools import reduce


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    temp = Solution()
    print(temp.groupAnagrams(strs))


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups: dict[str, list[str]] = dict()
        input_str: str
        for input_str in strs:
            # reduce only works when you have at least two values, anticipate empty strings
            # sorted_input_str = reduce(lambda x, y: x + y, sorted(input_str))
            sorted_input_str = "".join(sorted(input_str))
            if sorted_input_str in groups:
                groups[sorted_input_str].append(input_str)
            else:
                groups[sorted_input_str] = [input_str]

        group_list: list[list[str]] = list()
        for key in groups:
            group_list.append(groups[key])

        return group_list

if __name__ == "__main__":
    main()
