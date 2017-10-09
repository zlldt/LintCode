class Solution {
public:
    /*
     * @param num: a positive number
     * @return: true if it's a palindrome or false
     */
    bool isPalindrome(int num) {
        // Write your code here    
        int storage[32]={0};
        int i = 0, length = 0;
        for ( ; num > 9; )
        {
            storage[i] = num;
            num = num/10;
            i++;
        }
        storage[i]=num;
        length = i+1;
        for ( i = 0; i < length; i++)
        {
            if ( i == length-1-i)
            return true;
            if ( storage[i] != storage[length-1-i])
            return false;
        }
    }
};
