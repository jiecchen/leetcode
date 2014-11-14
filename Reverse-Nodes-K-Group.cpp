class Solution {
public:
    ListNode *reverseKGroup(ListNode *head, int k) {
      ListNode *start =  head; // point to the start of the k-interval
      ListNode *preStart = NULL;
      bool firstQ = true;
      while (start !=  NULL) {
	// check if still has k nodes
	int n = 0;
	ListNode *cur = start;
	while (n < k && cur != NULL) {
	  n++;
	  cur = cur->next;
	}
	if (n < k) {
	  return head;
	}
	
	// now have at least k nodes left
	ListNode *pre = cur;
	
	cur = start;
	
	for (int i = 0; i < k; ++i) {

	  ListNode *rec = cur->next;
	  cur->next = pre;
	  pre = cur;
	  cur = rec;
	}
	if (firstQ) {
	  firstQ = false;
	  head = pre;
	}
	else {
	  preStart->next = pre;
	}
     	preStart = start;
	start->next = cur;
	start = cur;      
      }
      return head;
    }
};






