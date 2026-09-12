class Solution {
    public int longestConsecutive(int[] nums) {
        int toRet = 0;
        HashSet<Integer> allNums = new HashSet();
        for(int num: nums){
            allNums.add(num);
        }

        for(int num: nums){
            if(!allNums.contains(num-1)){
                int curr = 1;
                while(allNums.contains(num+curr)){
                    curr+=1;
                }
                toRet = Math.max(toRet, curr);
            }
        }
        return toRet;
        
        
    }
}
