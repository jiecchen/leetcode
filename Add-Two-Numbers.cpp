#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    int inc = 0;
    ListNode *ans = new ListNode(0);
    ListNode *p = ans;
    ListNode *preP = NULL;
    while (l1 != NULL || l2 != NULL) {
      ListNode n1(0), n2(0);
      if (l1 == NULL) {
	n2 = *l2;
      }
      else if (l2 == NULL) {
	n1 = *l1;
      }
      else { // none of them is null
	n1 = *l1;
	n2 = *l2;
      }
      int sum = inc + n1.val + n2.val;
      p->val = sum % 10;
      inc = sum / 10;
      l1 = n1.next;
      l2 = n2.next;
      p->next = new ListNode(0);
      preP = p;
      p = p->next;
    }
    if (inc != 0) {
      p->val = inc;
    }
    else {
      delete p;
      preP->next = NULL;
    }
    return ans;
  }
};
