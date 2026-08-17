class Solution {
    public int[] runningSum(int[] nums) {
        int n = nums.length;
        int[] narr = new int[n];
        int i ;
        for(i=0 ; i<nums.length ; i++){
            if(i==0){
            narr[i] = nums[i];
        }
        else{
        narr[i] = narr[i-1] + nums[i];
        }
        }
        return narr;


        
    }
}