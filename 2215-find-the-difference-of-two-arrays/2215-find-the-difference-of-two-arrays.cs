public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
        // HashSet<int> uniqueNumbers = new HashSet<int>(numbers);
        HashSet<int> num1 = new HashSet<int>(nums1);
        HashSet<int> num2 = new HashSet<int>(nums2);
        int [] a = num1.Except(num2).ToArray();
        int [] b = num2.Except(num1).ToArray();
        return [a,b];
    }
}