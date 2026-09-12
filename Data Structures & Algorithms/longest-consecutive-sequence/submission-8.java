class Solution {
    public int longestConsecutive(int[] nums) {
        int longestSeq = 0;
        Arrays.sort(nums);
        ArrayList<Integer> all = new ArrayList();
       for(int num: nums){
        all.add(num);
       }

        System.out.println(all);

        int curr = 1;
        //[2,3,4,4,5,10,20]

        if(nums.length<=1){
            return nums.length;
        }

        for(int i=1; i<nums.length; i++){
            if(nums[i]==nums[i-1]+1){
                curr+=1;
            }
            else if(nums[i]==nums[i-1]){
                continue;
            }
            else{
                longestSeq = Math.max(curr, longestSeq);
                curr = 1;
            }
            
        }
        longestSeq = Math.max(longestSeq, curr);
        return longestSeq;
    }
}
