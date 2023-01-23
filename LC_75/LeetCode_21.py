def main():
    test = Solution()
    list1 = [1, 2, 4]
    head1 = ListNode(list1[0])
    tail1 = head1
    for i in range(1, len(list1)):
        tail1.next = ListNode(list1[i])
        tail1 = tail1.next
    list2 = [1, 3, 4]
    head2 = ListNode(list2[0])
    tail2 = head2
    for i in range(1, len(list2)):
        tail2.next = ListNode(list2[i])
        tail2 = tail2.next
    temp1 = head1
    while temp1 is not None:
        print(f'{temp1.val}, ', end='')
        temp1 = temp1.next

    print('\n')
    temp2 = head2
    while temp2 is not None:
        print(f'{temp2.val}, ', end='')
        temp2 = temp2.next

    print('\n\nmerged lists')
    head3 = test.mergeTwoLists(head1, head2)
    temp3 = head3
    while temp3 is not None:
        print(f'{temp3.val}, ', end='')
        temp3 = temp3.next

    # list3 = [1]
    # list4 = []
    # print(list3)
    # print(list4)
    # print(f'merged list: ', end='')
    # print(test.mergeTwoLists(list3, list4))


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # write a solution that actually uses linked lists
        merged_head = ListNode(0)
        merged_tail = merged_head

        # while both lists still have remaining nodes
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                merged_tail.next = list1
                list1 = list1.next
            else:
                merged_tail.next = list2
                list2 = list2.next
            merged_tail = merged_tail.next

        # at this point either one of the lists is exhausted or theyre both exhausted
        if list1 is None and list2 is not None:
            merged_tail.next = list2
        else:
            merged_tail.next = list1

        return merged_head.next


        # merged_head = ListNode(None, None)
        # merged_tail = None
        # pointer1 = list1
        # pointer2 = list2
        #
        # while pointer1 is not None or pointer2 is not None:
        #     # for the case that list1 is exhausted and list2 is not
        #     if pointer1 is None and pointer2 is not None:
        #         if merged_head.val is None:
        #             print(f'{pointer2.val}, ', end='')
        #             merged_head = ListNode(pointer2.val)
        #             merged_tail = merged_head
        #         else:
        #             print(f'{pointer2.val}, ', end='')
        #             temp = ListNode(pointer2.val)
        #             merged_tail.next = temp
        #             merged_tail = temp
        #         pointer2 = pointer2.next
        #     # for the case that list1 is not exhauted and list2 is
        #     elif pointer1 is not None and pointer2 is None:
        #         if merged_head.val is None:
        #             print(f'{pointer1.val}, ', end='')
        #             merged_head = ListNode(pointer1.val)
        #             merged_tail = merged_head
        #         else:
        #             print(f'{pointer1.val}, ', end='')
        #             temp = ListNode(pointer1.val)
        #             merged_tail.next = temp
        #             merged_tail = temp
        #         pointer1 = pointer1.next
        #     # for the case that neither list one nor two are exhausted
        #     else:
        #         if pointer1.val > pointer2.val:
        #             if merged_head.val is None:
        #                 print(f'{pointer2.val}, ', end='')
        #                 merged_head = ListNode(pointer2.val)
        #                 merged_tail = merged_head
        #             else:
        #                 print(f'{pointer2.val}, ', end='')
        #                 temp = ListNode(pointer2.val)
        #                 merged_tail.next = temp
        #                 merged_tail = temp
        #             pointer2 = pointer2.next
        #         else:
        #             if merged_head.val is None:
        #                 print(f'{pointer1.val}, ', end='')
        #                 merged_head = ListNode(pointer1.val)
        #                 merged_tail = merged_head
        #             else:
        #                 print(f'{pointer1.val}, ', end='')
        #                 temp = ListNode(pointer1.val)
        #                 merged_tail.next = temp
        #                 merged_tail = temp
        #             pointer1 = pointer1.next
        # return merged_head

        #
        # merged = list()
        # index1 = 0
        # index2 = 0
        #
        # while index1 < len(list1) or index2 < len(list2):
        #     # for the case that list1 is exhausted and list2 is not
        #     if index1 >= len(list1) and index2 < len(list2):
        #         # add an item from list 2 to the merged list
        #         merged.append(list2[index2])
        #         index2 += 1
        #     # for the case that list1 is not exhausted and list2 is
        #     elif index1 < len(list1) and index2 >= len(list2):
        #         # add an item from list 1 to the merged list
        #         merged.append(list1[index1])
        #         index1 += 1
        #     elif index1 < len(list1) and index2 < len(list2):
        #         if list1[index1] > list2[index2]:
        #             merged.append(list2[index2])
        #             index2 += 1
        #         else:
        #             merged.append(list1[index1])
        #             index1 += 1
        #     # find the list index that points to the
        #
        # return merged


if __name__ == "__main__":
    main()
