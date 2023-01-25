def main():
    test = Solution()

    list1 = [1, 2, 4, 5, 7]
    head1 = ListNode(list1[0])
    tail1 = head1
    looper = None
    for i in range(1, len(list1)):
        temp = ListNode(list1[i])
        if i == 2:
            looper = temp
        tail1.next = temp
        tail1 = tail1.next
    tail1.next = looper

    temp = head1
    for i in range(12):
        print(temp.val, end=", ")
        temp = temp.next
    print()

    temp = test.detectCycle(head1)
    print(temp.val)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # traversed = set()
        # pointer = head
        #
        # while pointer is not None:
        #     traversed.add(pointer)
        #     if pointer.next in traversed:
        #         return pointer.next
        #     pointer = pointer.next
        #
        # return None

        # try and use constant memory
        # theory, if you have a fast pointer and a slow pointer traveling the linked list, they will eventually run
        # into each other inside the loop. math can be used to help us determine where the loop starts from there

        slow = head
        fast = head

        # advance the pointers until they find the end of the array or they meet
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            # when the two pointers meet you can use some math to determine that the distance from the point that they
            # meet to the start of the loop is the same as the distance between the start of the list and the begining
            # of the loop. Reset the slow pointer to the head of the list and then reset the speed of fast to be the
            # same as slow. Increment fast and slow until they meet. This will be the start of the loop
            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast

        return None





if __name__ == "__main__":
    main()
