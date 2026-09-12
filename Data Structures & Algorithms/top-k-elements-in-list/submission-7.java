class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap();
        for(int num: nums){
            if(!freq.containsKey(num)){
                freq.put(num, 1);
            }
            else{
                freq.put(num, freq.get(num)+1);
            }
        }
        ArrayList<Integer>[] allVals = new ArrayList[nums.length+1];
        for(int i=0; i<allVals.length; i++){
            allVals[i] = new ArrayList();
        }
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            allVals[entry.getValue()].add(entry.getKey());
        }

        int[]res = new int[k];
        int index = 0;

        for(int i=allVals.length-1; i>0 && index<k; i--){
            for(int n: allVals[i]){
                res[index] = n;
                index+=1;
                if(index==k){
                    return res;
                }
            }
        }
        return res;

    }
}
