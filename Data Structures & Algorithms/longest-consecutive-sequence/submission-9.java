class Solution {
    public int longestConsecutive(int[] nums) {
        int longestSeq = 0;
        HashSet<Integer> allVals = new HashSet();
        for(int num: nums){
            allVals.add(num);
        }

        for(int i=0; i<nums.length; i++){
            if(!allVals.contains(nums[i]-1)){
                int curr = 1;
                while(allVals.contains(nums[i]+curr)){
                    curr+=1;
                }
                longestSeq = Math.max(longestSeq, curr);
            }
        }

        return longestSeq;


    
    }
}
