class Solution {
public:
    /*
     * @param n: An integer
     * @return: True or false
     */
    bool checkPowerOf2(int n) {
        // write your code here
        if( n<1 ){
            return false;
        }
        while(n>1){
            if(n%2==1)
            return false;
            n/=2;
        }
        return true;
    }
};
