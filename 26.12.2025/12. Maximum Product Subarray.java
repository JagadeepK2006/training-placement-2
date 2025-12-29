class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int max_prod = Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            int curr_prod = nums[i];
            for(int j=i+1;j<n;j++){
                curr_prod *= nums[j];
                max_prod = Math.max(max_prod, curr_prod);
            }
            max_prod = Math.max(max_prod, nums[i]);
        }
        return max_prod;
    }
}
