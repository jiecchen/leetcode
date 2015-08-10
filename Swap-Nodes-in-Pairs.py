# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        bak_head = head.next
        pre = None
        while head != None:
            if head.next == None:
                if pre != None:
                    pre.next = head
            else: # head.next != None
                nxt = head.next
                head.next = nxt.next
                nxt.next = head
                if pre != None:
                    pre.next = nxt
                pre = head
            head = head.next
        return bak_head
        


        # now change the direction in the list



def construct(lst):
    lst = [ListNode(x) for x in lst]
    for i in xrange(1, len(lst)):
        lst[i - 1].next = lst[i]
    return lst[0]

def print_lst(head):
    while head != None:
        print head.val
        head = head.next

sl = Solution()
head = construct([1, 2, 3, 4, 5])
new_head = sl.swapPairs(head)
print_lst(new_head)
