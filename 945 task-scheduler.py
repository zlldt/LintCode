class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        length = len(tasks)
        if n==0:
            return length
        dict = {}
        for i in tasks:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1

        taskcount=sorted(dict.values(),reverse=True)
        maxcount = taskcount.count(taskcount[0])
        if len(taskcount)==1:
            return (taskcount[0]-1)*(n+1)+1
        if maxcount>1:
            if (taskcount[0]-1)*(n+1)+maxcount-1>=length:
                return (taskcount[0]-1)*(n+1)+maxcount
        else:
            if (taskcount[0]-1)*(n+1)+1>=length:
                return (taskcount[0]-1)*(n+1)+1
