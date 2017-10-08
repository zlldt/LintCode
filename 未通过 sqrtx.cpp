class Solution {
public:
    /*
     * @param x: An integer
     * @return: The sqrt of x
     */
    int sqrt(int x) {
        // write your code here
        int sqrt_base=1;
        sqrt_base=x/2;
        while(x>1000000)
            sqrt_base=1000;
        while( sqrt_base*sqrt_base > x )
        {
            sqrt_base/=2;
        }
        while( sqrt_base*sqrt_base < x )
        {
            while(sqrt_base*sqrt_base<(x/4))
            sqrt_base*=2;
            sqrt_base++;
        }
        if( sqrt_base*sqrt_base == x )
        return sqrt_base;
        if((sqrt_base*sqrt_base < x) && ((sqrt_base+1)*(sqrt_base+1) > x))
        return sqrt_base;
    }
};
