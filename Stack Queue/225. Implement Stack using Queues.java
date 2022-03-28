# pop: time complexity: O(n)
# other methods: time complexity: O(1)

class MyStack {
    
    private Queue<Integer> q;
    int top_ele = 0;
    public MyStack() {
        q = new LinkedList<>();
    }
    
    public void push(int x) {
        q.add(x);
        top_ele = x;
    }
    
    public int pop() {
        int s = q.size();
        while (s > 2) {
            q.offer(q.poll());
            s--;
        }
        
        top_ele = q.peek();
        q.offer(q.poll());
        
        return q.poll();
    }
    
    public int top() {
        return top_ele;
    }
    
    public boolean empty() {
        return q.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */