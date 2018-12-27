class Solution:
    """
    @param lower: Integer : lower bound
    @param upper: Integer : upper bound
    @return: a list of every possible Digit Divide Numbers
    """
    def digitDivideNums(self, lower, upper):
        # write your code here
        result = []
        for i in range(lower,upper+1):
            if self.check(i):
                result.append(i)
        return result

    def check(self, i):
        number = i
        while number>9:
            digit=number%10
            number = number//10
            if digit==0 or i%digit:
                return False
        if i%number:
            return False
        return True
