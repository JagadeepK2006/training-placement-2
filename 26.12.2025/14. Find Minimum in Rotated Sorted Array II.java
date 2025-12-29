class Solution {
    public int findMin(int[] nums) {
       int low=0;
       int high=nums.length-1;
       if(nums.length==1) return nums[0];
       if(nums.length==2) return Math.min(nums[0],nums[1]);

       while(low<=high)
       {
        int mid = low +(high-low)/2;
        if(low==high) return nums[low];
         if(low==high) return nums[low];
         if(high-low+1==2) return Math.min(nums[low],nums[high]);
        if(nums[low]==nums[mid] && nums[mid]==nums[high])
        {
            high--;
            low++;
            continue;
           
            
        }
        if(mid == 0 || mid == nums.length-1)
        {
            return nums[mid];
        }
        
        if(nums[mid]<nums[mid-1] && nums[mid+1]>=nums[mid])
        {
            return nums[mid];
        }
        else if(nums[mid]>nums[high])
        {
            low=mid+1;
        }
        else
        {  
            
            high=mid;
        }

       


       } 
       return nums[low];
    }
}
