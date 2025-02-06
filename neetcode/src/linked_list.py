from typing import List


class ListNode:
    """Node class for internal use for singly linked list

        Attributes:
        val (int): Value stored in node.
        next (ListNode): next item in list. None if this node is the tail of the list.
    """

    def __init__(self, val, next_node=None):
        """
            Create new node with integer val and ListNode or None for tail
            Args:
                val (int): integer value contained in this node.
                next_node (str): The value for the second attribute.
        """
        self.val = val
        self.next = next_node


class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insert_head(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insert_tail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def get_values(self) -> List[int]:
        curr = self.head.next
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next

        print(output)
        return output
