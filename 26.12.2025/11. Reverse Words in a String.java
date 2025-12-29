class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        String[] arr = s.split("\\s+");
        String rev = "";
        
        for(int i=arr.length-1;i>=0;i--){
            if(arr[i]!=arr[0]) {
                rev=rev+arr[i]+" ";
            }else{
                rev=rev+arr[i];
            }
        }
        return rev;
    }
}
