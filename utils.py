class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def construct_linked_list(lst):
    """
    Given a list, return a linked list
    """
    lst = [ListNode(x) for x in lst]
    for i in xrange(1, len(lst)):
        lst[i - 1].next = lst[i]
    return lst[0]

def print_linked_list(head):
    """
    Print the given linked list
    """
    while head != None:
        print head.val
        head = head.next
