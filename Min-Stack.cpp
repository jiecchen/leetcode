#include <stack>
#include <vector>

class MinStack {
public:
  void push(int x) {
    stk.push(x);
    if (min.empty() || min.top() >= x)
      min.push(x);
  }
  
  void pop() {
    if (min.top() == stk.top())
      min.pop();
    stk.pop();
  }
  
  int top() {
    return stk.top();
  }
  
  int getMin() {
    return min.top();
  }
private:
  std::stack<int> stk;
  std::stack<int> min;
};



