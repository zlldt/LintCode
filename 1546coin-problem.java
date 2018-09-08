public class Solution {
    /**
     * @param n: The guest paid
     * @param m: the price
     * @return: the sum of the number of banknotes
     */
    public int coinProblem(int n, int m) {
        // Write your code here
        int sum=0;
        int value = n - m;
        int[] changes = {100,50,20,10,5,2,1};
        for(int i=0; i<changes.length; i++){
            if (value >= changes[i]){
                sum += value/changes[i];
                value = value%changes[i];
            }
            if(value==0)
                break;
        }
        return sum;
    }
}
