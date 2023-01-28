def main():
    s = "anagram"
    t = "nagaram"
    s1 = "cat"
    t1 = "tree"
    temp = Solution()
    print(temp.isAnagram(s, t))
    print(temp.isAnagram(s1, t1))


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = dict()
        t_dict = dict()

        for char in s:
            if char in s_dict:
                s_dict[char] = s_dict[char] + 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict:
                t_dict[char] = t_dict[char] + 1
            else:
                t_dict[char] = 1

        num_chars_s = s_dict.__len__()
        num_chars_t = t_dict.__len__()

        if num_chars_s != num_chars_t:
            return False

        for key in s_dict.keys():
            if key not in t_dict:
                return False
            elif s_dict[key] != t_dict[key]:
                return False

        return True


if __name__ == "__main__":
    main()
