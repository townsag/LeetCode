"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character may map to itself.

No two charecters may map to the same charecter
"""


def main():
    test = Solution()
    print(test.isIsomorphic("egg", "add"), end='\n\n')
    print(test.isIsomorphic('foo', 'bar'), end='\n\n')
    print(test.isIsomorphic('badc', 'baba'), end='\n\n')

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping: dict[str: str] = dict()            # contains the character in t that a character in s maps to
        reverse_mapping: dict[str: str] = dict()    # contains the character in s that a character in t maps to
        if len(s) != len(t):
            return False

        for index in range(len(s)):
            print(str(index))
            if s[index] not in mapping:
                # check to see if the character in t is already mapped to by another character in s
                if t[index] in reverse_mapping:
                    return False
                # add that character mapping to the dictionary
                mapping[s[index]] = t[index]
                reverse_mapping[t[index]] = s[index]
            else:
                # check that this index matches existing mapping
                print(f's[index]: {s[index]}')
                print(f't[index]: {t[index]}')
                if mapping[s[index]] is not t[index]:
                    return False

        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
