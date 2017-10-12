class Solution {
public:
    /*
     * @param chars: The letter array you should sort by Case
     * @return: nothing
     */
    void swap(string &chars,int p,int q){
        char temp;
        if(chars[p]>='A' && chars[p]<='Z' && chars[q]>='a' && chars[q]<='z')
        {
            temp=chars[p];
            chars[p]=chars[q];
            chars[q]=temp;
        }
    }
    void sortLetters(string &chars) {
        // write your code here
        if(chars.length()==0)
        return;
        int lower,higher;
        for(lower=0;lower<=chars.length()-1;lower++)
        {
            for(higher=lower+1;higher<=chars.length()-1;higher++)
            {
                swap(chars,lower,higher);
            }
        }
    }
};
