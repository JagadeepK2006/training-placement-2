class Solution {
    public int arrangeCoins(int n) {
        long a=n;
      a= (long)((Math.sqrt(1+8*a)-1)/2);
      
      return (int)a;
    }
}
