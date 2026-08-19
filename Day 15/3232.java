class Solution {
    public boolean canAliceWin(int[] nums) {

        int singlesum = 0;
        int doubleintsum = 0;

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] <= 9) {
                singlesum += nums[i];
            } else {
                doubleintsum += nums[i];
            }
        }

        if (singlesum == doubleintsum) {
            return false;
        } else {
            return true;
        }
    }
}