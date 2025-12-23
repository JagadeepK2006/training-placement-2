class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int n = nums.length;
        int maxCount = 0;
        
        for (int i = 0; i < n; i++) {
            int currentCount = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == 1) {
                    currentCount++;
                    maxCount = Math.max(maxCount, currentCount);
                } else {
                    break;
                }
            }
        }
        
        return maxCount;
    }
}
