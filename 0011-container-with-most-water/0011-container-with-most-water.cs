public class Solution {
    public int MaxArea(int[] height) {
        int max = 0;
        int left = 0;
        int min = 0;
        int right = height.Length - 1;
        while( left<right){
            if (height[left] < height[right]){
                min = height[left];
                max = Math.Max(min*(right-left), max);
                left++;
            }
            else{
                min = height[right];
                max = Math.Max(min*(right-left), max);
                right--;
            }
            // min = Math.min(height[left], height[right])
            
        }
        return max;
    }
}