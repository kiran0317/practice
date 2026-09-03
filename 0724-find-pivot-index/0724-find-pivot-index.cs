public class Solution {
    public int PivotIndex(int[] nums) {
         int sum=0;
       foreach (int e in nums){
           sum+=e;
       }
       int ls=0;
       for(int i=0;i<nums.Length;i++){
           
           sum=sum-nums[i];
           if(ls==sum)
           return i;
           ls+=nums[i];
       }
       return -1;
    }
}