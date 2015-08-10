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
        







