class Solution {
public:
    /*
     * @param A: an integer array
     * @return: 
     */
    void sortIntegers(vector<int> &A) {
        // write your code here
        int count1,count2,temp=0;
        if(A.empty())
        return;
        for(count1=0;count1<(A.size()-1);count1++)
        {
            for(count2=count1+1;count2<A.size();count2++)
            {
                if(A[count1]>A[count2])
                {
                    temp=A[count1];
                    A[count1]=A[count2];
                    A[count2]=temp;
                }
            }
        }
    }
};
