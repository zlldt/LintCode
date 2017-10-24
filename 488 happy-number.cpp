class Solution {
public:
    /*
     * @param n: An integer
     * @return: true if this is a happy number or false
     */
    int calc(int n){
        int lower=0,sum=0;
        for(;n>9;){
            lower=n%10;
            n/=10;
            sum+=lower*lower;
        }
        sum+=n*n;
        return sum;
    }
    bool isHappy(int n) {
        // write your code here
        if(n==3||n==4||n==5)
        return false;
        while(n>2){
            if(n==3||n==4||n==5)
        	return false;
            n=calc(n);
        }
        if(n!=1)
        return false;
        if(n==1)
        return true;
    }
};
