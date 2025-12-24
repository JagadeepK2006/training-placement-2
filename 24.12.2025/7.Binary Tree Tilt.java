class Solution { 
    int ans = 0;
    
    public int findTilt(TreeNode root) {
        difference(root);
        return ans;
    }

    public int difference(TreeNode root) {
        if (root == null) return 0; 

        int left = difference(root.left);   
        int right = difference(root.right);

        ans += Math.abs(left - right);     
        return left + right + root.val;     
    }
}
