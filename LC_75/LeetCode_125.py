from functools import reduce


def main():
    s = "A man, a plan, a canal: Panama"
    temp = Solution()
    print(temp.isPalindrome(s))


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove all non-alphanumeric charecters from string
        sub_str = ''.join(filter(str.isalnum, str(s)))
        sub_str = sub_str.lower()
        print(sub_str)
        head = 0
        tail = len(sub_str) - 1

        while head < tail:
            if sub_str[head] is not sub_str[tail]:
                return False
            head += 1
            tail -= 1

        return True


if __name__ == "__main__":
    main()
