class Solution:
    """
    @param n: the number of keys
    @param m: the number of locks
    @return: the numbers of open locks
    """
    def unlock(self, n, m):
        # Write your code here
        state= [0 for x in range(m + 1)]
        for key in range(1,n+1):
            for lock in range(key,m+1,key):
                state[lock]=state[lock]^1
        return state.count(1)
