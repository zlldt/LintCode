class Solution {
public:
    /*
     * param k : As description.
     * param n : As description.
     * return: How many k's between 0 and n.
     */
    int digitCounts(int k, int n) {
        // write your code here
        int count = 0;
        int number = 0;
        for ( ; number < n+1 ; number++ ){
            if ( number == k)
            count++;
            if (number>=10){
            if ( (number/10) == k)
            count++;
            }
            if(number>=100){
            if ( (number/100) == k)
            count++;
            }
            if(number>=1000){
            if ( (number/1000) == k)
            count++;
            }
            if(number>=10000){
            if ( (number/10000) == k)
            count++;
            }
        }
        return count;
    }
};
