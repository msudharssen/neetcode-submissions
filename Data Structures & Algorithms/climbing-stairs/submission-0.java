class Solution {
    public int climbStairs(int n) {
        if(n==1)return 1;
        if(n==2)return 2;
        if(n==3) return 3;

        int[]nums = new int[n];
        nums[0] = 1;
        nums[1] = 2;
        nums[2] = 3;

        for(int i=3; i<nums.length; i++){
            nums[i] = nums[i-1] +nums[i-2];
        }

        return nums[n-1];
        
    }
}
