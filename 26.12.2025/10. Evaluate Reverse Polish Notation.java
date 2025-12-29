class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();
        for (int i=0; i<tokens.length; i++) {
            String curr = tokens[i];
            if (curr.equals("+") || curr.equals("-") || curr.equals("*") || curr.equals("/")) {
                int b = s.pop();
                int a = s.pop();
                int ans = 0;
                if (curr.equals("+")) ans = a+b;
                else if(curr.equals("-")) ans = a-b;
                else if (curr.equals("*")) ans = a*b;
                else ans = (int) a/b;
                s.push(ans);
            } else {
                s.push(Integer.parseInt(tokens[i]));
            }
        }
        return s.pop();
    }
}
