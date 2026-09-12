class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList();
        ans.add(new ArrayList());
        ans.get(0).add(1);
        
        for(int i=1; i<numRows; i++){
            List<Integer> prev = new ArrayList(ans.get(i-1));
            prev.add(0,0);
            prev.add(0);
            List<Integer> toAdd = new ArrayList();
            for(int j=1; j<prev.size(); j++){
                toAdd.add(prev.get(j) + prev.get(j-1));
            }
            ans.add(toAdd);
        }
        return ans;
    }
}