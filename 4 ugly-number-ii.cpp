class Solution {
public:
    /*
     * @param n: An integer
     * @return: the nth prime number as description.
     */
    int nthUglyNumber(int n) {
        // write your code here
        int UglyNumber[65535]={1,2,3,4,5};
        int temp=0,count,i;
        if ( n == 1 )
        {
            return 1;
        }
        if ( n == 2 )
        {
            return 2;
        }
        if ( n == 3 )
        {
            return 3;
        }
        if ( n == 4 )
        {
            return 4;
        }
        if ( n == 5 )
        {
            return 5;
        }
        for( i=6;i<n+1;i++)
        {
            for(count=0;count<i;count++)
            {
                if( UglyNumber[count]*2>UglyNumber[i-2] )
                {
                    temp=UglyNumber[count]*2;
                    break;
                }
            }
            for(count=0;count<i;count++)
            {
                if( UglyNumber[count]*3>UglyNumber[i-2] )
                {
                    if( temp>UglyNumber[count]*3 )
                    {
                        temp=UglyNumber[count]*3;
                    }
                    break;
                }
            }
            for(count=0;count<i;count++)
            {
                if( UglyNumber[count]*5>UglyNumber[i-2] )
                {
                    if( temp>UglyNumber[count]*5 )
                    {
                        temp=UglyNumber[count]*5;
                    }
                    break;
                }
            }
            UglyNumber[i-1]=temp;
        }
        return UglyNumber[n-1];
    }
};
