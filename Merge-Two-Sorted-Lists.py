import utils
from utils import ListNode

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        cur = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        while l1 != None:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2 != None:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return head



s = Solution()
l1 = utils.construct_linked_list([1, 3, 10, 20])
l2 = utils.construct_linked_list([2, 4, 5, 6, 100])

utils.print_linked_list(l1)
print '\n'
utils.print_linked_list(l2)
print '\n'
utils.print_linked_list(s.mergeTwoLists(l1, l2))
