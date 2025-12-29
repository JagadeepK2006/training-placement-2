class Solution {
    List<Integer> ans=new ArrayList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        next(root);
        return ans;

    }
    private void next(TreeNode curr){
        if(curr==null)return;
        ans.add(curr.val);
        next(curr.left);
        next(curr.right);
    }
}
