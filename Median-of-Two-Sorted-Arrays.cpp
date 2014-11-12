class Solution {
public:
  double findMedianSortedArrays(int A[], int m, int B[], int n) {
    // boundary cases
    if (m == 0){
      return (B[n >> 1] + B[(n - 1) >> 1]) / 2.0;
    }
    if (n == 0){
      return (A[m >> 1] + A[(m - 1) >> 1]) / 2.0;
    }
    //
    int p1 = (n + m) >> 1;
    int p2 = (n + m - 1) >> 1; 
    return ( searchK(A, m, B, n, p1) + searchK(A, m, B, n, p2) ) / 2.0;
  }

  // search the k smallest number in the merge of A and B, count from 0
  double searchK(int A[], int m, int B[], int n, int k){
    int l, r, mid;

    // assume in A[]
    l = 0;
    r = m;
    int gap = 10000001;
    while (r - l > 0) {
      if (r - l == gap) break;
      gap = gap > r - l ? r - l : gap;
      mid = (r + l) >> 1;
      int nsma = lbsearch(A[mid], B, n);
      int nseq = rbsearch(A[mid], B, n);
      if (nsma + mid > k) {
	r = mid;
      } 
      else if (nseq + mid < k) {
	l = mid;
      }

      if (nsma + mid <= k && nseq + mid >= k) {
	return A[mid];
      }
    }

    // assume in B[]
    l = 0;
    r = n;
    gap = 100000001;
    while (r - l > 0) {
      if (r - l == gap) break;
      gap = gap > r - l ? r - l : gap;
      mid = (r + l) >> 1;
      int nsma = lbsearch(B[mid], A, m);
      int nseq = rbsearch(B[mid], A, m);
      if (nsma + mid > k) {
	r = mid;
      } 
      else if (nseq + mid < k) {
	l = mid + 1;
      }
      if (nsma + mid <= k && nsma + mid >= k)
	return B[mid];
    }
  }

  // return # of int that < a
  int lbsearch(const int a, int C[], int len){
    int l = -1;
    int r = len;
    int mid;
    do {
      mid = (l + r) >> 1;
      if (C[mid] < a)
	l = mid;
      else
	r = mid;
    } while (r - l > 1);
    return l + 1;
  }

  // return # of int that <= a
  int rbsearch(int a, int C[], int len){
    int l = -1;
    int r = len;
    int mid;
    do {
      mid = (l + r) >> 1;
      if (C[mid] <= a)
	l = mid;
      else
	r = mid;
    } while (r - l > 1);
    return l + 1;
  }
};






