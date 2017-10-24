class Solution {
public:
    /*
     * @param num: An integer
     * @return: true if num is an ugly number or false
     */
    bool isUgly(int num) {
        // write your code here
        if(num<=0)
            return false;
        if(num==1)
            return true;
        if(num==2)
            return true;        
        if(num==3)
            return true;
        if(num==4)
            return false;
        if(num==5)
            return true;
            
        while(num%5==0 || num%3==0 || num%2==0){
            if(num%5==0)
            num/=5;
            if(num%3==0)
            num/=3;
            if(num%2==0)
            num/=2;
        }
        if(num>5)
        return false;
    }
};
