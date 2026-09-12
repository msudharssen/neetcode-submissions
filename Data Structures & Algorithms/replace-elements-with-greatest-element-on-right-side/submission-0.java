class Solution {
    public int[] replaceElements(int[] arr) {
        int[]copy = new int[arr.length];

        copy[copy.length-1] = -1;

        for(int i=copy.length-2; i>=0; i--){
            copy[i] = Math.max(copy[i+1], arr[i+1]);
        }

        return copy;
    }
}