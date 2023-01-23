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
    def reverseList(self, head):
        iterator = head
        values = list()
        while iterator is not None:
            values.append(iterator.val)
            iterator = iterator.next

        return_head = ListNode(0)
        iterator = return_head
        for index in range(len(values)):
            iterator.next = ListNode(values.pop())
            iterator = iterator.next

        return return_head.next



if __name__ == "__main__":
    main()