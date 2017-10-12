class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer
     */
    int Up2(int n){
        if(n==2)
        {
            return 1;
        }
        if(n==3)
        {
            return 1;
        }
        if(n>3)
        {
            return Up1(n-1);
        }
    }
    int Up1(int n){
        if(n==2)
        {
            return 1;
        }
        if(n==3)
        {
            return 2;
        }
        if(n==4)
        {
            return 3;
        }        
        if(n>4)
        {
//            return Up1(n-1)+Up2(n-1);
            return 2*Up1(n-2)+Up2(n-2);
        }
    }
    int climbStairs(int n) {
        // write your code here
        if(n==0)
        {
            return 0;
        }
        if(n==1)
        {
            return 1;
        }        
        if(n==2)
        {
            return 2;
        }
        if(n==3)
        {
            return 3;
        }
        if(n>3)
        {
            return(Up1(n)+Up2(n));
        }
    }
};
