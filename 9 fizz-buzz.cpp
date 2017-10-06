class Solution {
public:
    /*
     * @param n: An integer
     * @return: A list of strings.
     */
    vector<string> fizzBuzz(int n) {
        vector<string> v(n);
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                v[i-1]="fizz buzz";
            } else if (i % 5 == 0) {
                v[i-1]="buzz";
            } else if (i % 3 == 0) {
                v[i-1]="fizz";
            } else {
                v[i-1]=to_string(i);
            }
        }
        return v;
    }
};
