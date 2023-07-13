# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    lst = []
    while head:
        if head in lst:
            return 1
        lst.append(head)
        head = head.next
    return 0
