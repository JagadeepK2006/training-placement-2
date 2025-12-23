class Solution {
    public String licenseKeyFormatting(String s, int k) {
        int len = s.length();
        StringBuilder sb = new StringBuilder();
        for (int i = len - 1, l = 0; i >= 0; --i) {
            char c = s.charAt(i);
            if (c == '-') continue;
            sb.append(getChar(c));
            if (++l == k) {
                sb.append('-');
                l = 0;
            }
        }
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '-') 
            sb.deleteCharAt(sb.length() - 1);
        return sb.reverse().toString();
    }
    private char getChar(char c) {
        if ((c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z')) return c;
        return (char)(c - 32);
    }
}
