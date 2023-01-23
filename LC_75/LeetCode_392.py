def main():
    test = Solution()
    print('should be True')
    print(test.isSubsequence('abc', 'ahbgdc'))
    print('should be True')
    print(test.isSubsequence('abc', 'abc'))
    print('should be False')
    print(test.isSubsequence('axc', 'ahbgdc'))
    print('should be False')
    print(test.isSubsequence('abd', 'axb'))
    print('should be False')
    print(test.isSubsequence('b', 'c'))


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # instead try iterating through the string not the substring
        s_index = 0
        for t_index in range(len(t)):
            if s_index < len(s):
                if s[s_index] is t[t_index]:
                    s_index += 1

        if s_index is len(s):
            return True
        return False


        # t_index = 0
        #
        # # substring index points to new unchecked character
        # # string index points to new unchecked character
        # for index in range(len(s)):
        #     if t_index >= len(t):
        #         return False
        #
        #     found = False
        #     # check to see if the current substring index matches the current string index
        #     if s[index] is t[t_index]:
        #         found = True
        #         # advance the substring index
        #         t_index += 1
        #         continue
        #
        #     # if the character at the string index is not the same as the unchecked substring character
        #     # advance the string index until either the characters of both strings match or the string index
        #     # is off the range
        #     while t_index < len(t) and not found:
        #         if s[index] is t[t_index]:
        #             found = True
        #             t_index += 1
        #             break
        #         t_index += 1
        #
        #     if t_index >= len(t) and not found:
        #         return False
        #
        # return True



if __name__ == '__main__':
    main()

