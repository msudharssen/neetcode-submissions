class MyHashMap {
    HashMap<Integer, Integer> allVals;

    public MyHashMap() {
        this.allVals = new HashMap();
        
    }
    
    public void put(int key, int value) {
        this.allVals.put(key, value);
    }
    
    public int get(int key) {
        if(this.allVals.containsKey(key)){
            return this.allVals.get(key);
        }
        return -1;
    }
    
    public void remove(int key) {
        if(this.allVals.containsKey(key))this.allVals.remove(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */