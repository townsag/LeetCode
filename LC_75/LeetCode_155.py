import sys


def main():
    s = "()"
    s1 = "(())"
    s3 = "(([))"


class MinStack(object):

    def __init__(self):
        self.data = list()
        self.current_min = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.data) == 0:
            self.current_min.append(val)
        else:
            self.current_min.append(min(self.current_min[-1], val))
        self.data.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.current_min.pop()
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.current_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    main()
