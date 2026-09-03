public class Solution {
    public int LargestAltitude(int[] gain) {
        int n = gain.Length;
        int ans = 0;
        int sum = 0;
        foreach (int ele in gain ){
            sum += ele;
            if (ans < sum) {
                ans = sum;
            }
        }
        return ans;
    }
}