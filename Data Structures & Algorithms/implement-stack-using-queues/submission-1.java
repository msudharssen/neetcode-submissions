class MyStack {
    ArrayList<Integer> myQ;

    public MyStack() {
        this.myQ = new ArrayList();
    }
    
    public void push(int x) {
        this.myQ.add(x);
    }
    
    public int pop() {
        for(int i=0; i<this.myQ.size()-1; i++){
            this.myQ.add(this.myQ.remove(0));
        }
        return this.myQ.remove(0);
    }
    
    public int top() {
        return this.myQ.get(this.myQ.size()-1);
    }
    
    public boolean empty() {
        return this.myQ.size() == 0;
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