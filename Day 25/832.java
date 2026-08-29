class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int[][] output = new int[image.length][image[0].length];
        for (int i = 0; i < image.length; i++) {
            int k = 0;
            for (int j = image[i].length - 1; j >= 0; j--) {

                if (image[i][j] == 0) {
                    output[i][k] = 1;
                } else {
                    output[i][k] = 0;
                }
                k++;
            }
        }
        return output;
    }
}
