class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ret = 0;

        for(int i=0; i<nums.length; i++){
            if(nums[i]==1){
                int temp = 1;
                int read = i+1;
                while(read < nums.length){
                    if (nums[read]==1){
                        temp+=1;
                        read+=1;
                    }
                    else{
                        i=read;
                        break;
                    }
                }
                ret = Math.max(ret, temp);
            }

        }
        return ret;

}
}