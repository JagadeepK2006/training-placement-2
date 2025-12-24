class Solution {
    public String reverse(String s, int l, int r){
        char[] str = s.toCharArray();
        r = Math.min(r, s.length()-1);
        while(l<r){
            char temp = str[l];
            str[l] = str[r];
            str[r] = temp;
            l++;
            r--;
        }
        return new String(str);
    }
    public String reverseStr(String s, int k) {
        int left = 0;
        int right = k-1;
        if(k>=s.length()) return reverse(s, 0, s.length()-1);
        while(left<s.length()){
            s = reverse(s, left, right); 
            left = left+(2*k); 
            right = right+(2*k); 
        }
        return s;
    }
}
