class Solution {
public:
    /*
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &numbers, int target) {
        // write your code here
        int index1=0,index2=0;
        for(;index1<numbers.size()-1;index1++){
            for(index2=index1+1;index2<=numbers.size()-1;index2++)
            {
                if(target==(numbers[index1]+numbers[index2]))
                {
                    return {index1+1,index2+1};
                }
            }
        }
        return {};
    }
};
