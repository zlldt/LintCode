class Solution {
public:
    /*
     * @param n: An integer
     * @param nums: An array
     * @return: the Kth largest element
     */
    int kthLargestElement(int n, vector<int> &nums) {
        // write your code here
        int count=0,large;
        int temp;
        for(;count<nums.size()-1;count++)
        {
            for(large=count+1;large<nums.size();large++)
            {
                if(nums[count]<nums[large])
                {
                    temp=nums[count];
                    nums[count]=nums[large];
                    nums[large]=temp;
                }
            }
        }
        return nums[n-1];
    }
};
