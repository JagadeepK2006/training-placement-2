class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length-1;
        
        while(low <= high){
            int mid = (high - low)/2 + low;
            if(nums[low] <= nums[mid] && nums[mid] <= nums[high]){
                return nums[low];
            }
            if(nums[mid] <= nums[high]){
                
                high = mid;
            }else{
                
                low = mid+1;
            }
        }
        return -1;
    }
}
