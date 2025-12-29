class Solution {

    boolean isCollinear(int[] point1, int[] point2, int[] point3) {
        return point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1])
                + point3[0] * (point1[1] - point2[1]) == 0;
    }

    public int maxPoints(int[][] points) {
        int best = Math.min(points.length, 2);
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                int collinear = 0;
                for (int k = j + 1; k < points.length; k++) {
                    if (k == i || k == j)
                        continue;
                    if (isCollinear(points[i], points[j], points[k])) {
                        collinear++;
                    }
                }
                best = Math.max(best, collinear + 2);
            }
        }
        return best;
    }
}
