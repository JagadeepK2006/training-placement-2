class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n = strs.length;
        if (n == 0) return "";

       
        int minLen = strs[0].length();
        for (int i = 1; i < n; i++) {
            minLen = Math.min(minLen, strs[i].length());
        }

        char[] arr = new char[n];
        String result = "";

        for (int i = 0; i < minLen; i++) {

           
            for (int j = 0; j < n; j++) {
                arr[j] = strs[j].charAt(i);
            }

           
            for (int k = 0; k < n - 1; k++) {
                if (arr[k] != arr[k + 1]) {
                    return result;
                }
            }

            
            result += arr[0];
        }

        return result;
    }
}
