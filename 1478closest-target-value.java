import java.util.Arrays;

public class Solution {
    /**
     * @param target: the target
     * @param array: an array
     * @return: the closest value
     */
    public int closestTargetValue(int target, int[] array) {
        // Write your code here
        Arrays.sort(array);
        int i=0;
        int j=1;
        int sum = array[0]+array[1];
        if (sum>target){
            return -1;
        }
        for (;i<array.length-1;i++){
            for (j=i+1;j<array.length;j++){
                if(array[i]+array[j]>sum && array[i]+array[j]<=target){
                    sum = array[i]+array[j];
                }
                if(sum==target){
                    return target;
                }
            }
        }
        return sum;
    }
}
