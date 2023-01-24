def main():
    test = Solution()

    list1 = [1, 2, 4]
    head1 = ListNode(list1[0])
    tail1 = head1
    for i in range(1, len(list1)):
        tail1.next = ListNode(list1[i])
        tail1 = tail1.next

    reversed_list = test.reverseList(head1)
    temp = reversed_list
    while temp is not None:
        print(temp.val, end=", ")
        temp = temp.next
    print()


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # travers the whole list, storing each pointer
        # return the pointer to the middle mode
        # pointers = list()
        # temp = head
        # pointers.append(temp)
        # while temp.next is not None:
        #     temp = temp.next
        #     pointers.append(temp)
        #
        # return pointers[ceil_div(len(pointers) - 1, 2)]

        # try two pointers approach
        # 1 2 3 4 5
        slow = head
        fast = head
        while fast.next is not None:
            if fast.next.next is None:
                fast = fast.next
                slow = slow.next
            else:
                fast = fast.next.next
                slow = slow.next
        return slow


def ceil_div(a, b):
    return -(a // -b)


if __name__ == "__main__":
    main()
