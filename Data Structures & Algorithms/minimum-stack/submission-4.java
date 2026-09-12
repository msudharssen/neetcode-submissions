class MinStack {
    Stack<Integer> allVals; 
    Stack<Integer> minVals; 

    public MinStack() {
        this.allVals = new Stack();
        this.minVals = new Stack();
    }
    
    public void push(int val) {
        this.allVals.push(val);
        if(this.minVals.isEmpty()) {
            this.minVals.push(val);
        }
        else{
            int temp = Math.min(val, this.minVals.peek());
            this.minVals.push(temp);
        }
    }
    
    public void pop() {
        if(this.allVals.isEmpty()) return;
        this.allVals.pop();
        this.minVals.pop();
        
    }
    
    public int top() {
        return this.allVals.peek();
        
    }
    
    public int getMin() {
        return this.minVals.peek();
        
    }
}
