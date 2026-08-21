class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {

        int rows = matrix.length;
        int cols = matrix[0].length;

        List<Integer> nums = new ArrayList<>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {

                int current = matrix[i][j];

                boolean rowMin = true;
                boolean colMax = true;

                // current element row ka minimum hai?
                for (int k = 0; k < cols; k++) {
                    if (matrix[i][k] < current) {
                        rowMin = false;
                        break;
                    }
                }

                // current element column ka maximum hai
                for (int k = 0; k < rows; k++) {
                    if (matrix[k][j] > current) {
                        colMax = false;
                        break;
                    }
                }

                if (rowMin && colMax) {
                    nums.add(current);
                }
            }
        }

        return nums;
    }
}