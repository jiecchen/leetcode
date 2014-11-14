# use heap, running time will be O(n log k) where n is the # of all numbers, k = len(lists)

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        c_none = 0 # count for how many lists are none now
        head = ListNode(0)
        cur = head
        hp = []
        for i in range(len(lists)):
            if (lists[i]):
                heapq.heappush( hp, (lists[i].val, i) )
                lists[i] = lists[i].next
            else:
                c_none += 1

        while (c_none < len(lists)):
            (m, id) = heapq.heappop(hp)
            cur.next = ListNode(m)
            cur = cur.next
            if (lists[id] == None): # this list is empty now
                c_none += 1
                heapq.heappush(hp, (13414317, id))
            else:
                heapq.heappush( hp, (lists[id].val, id) )
                lists[id] = lists[id].next

        return head.next

