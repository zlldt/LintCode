class Solution {
public:
    /*
     * @param n: An integer
     * @return: An integer, denote the number of trailing zeros in n!
     */
    long long trailingZeros(long long n) {
            //return n/5+n/100+n/1000+n/10000;

    long long count=0,max=n;
    long long divide=1;
    for(;max>5;max=max/5)
    {
        divide=divide*5;
    }
    for(;divide>1;divide=divide/5)
    {
        count+=n/divide;
    }
    return count;

    }
};
