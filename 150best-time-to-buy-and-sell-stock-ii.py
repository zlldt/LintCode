class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices == []:
            return 0
        profits = 0
        lowest = prices[0]
        previous = prices[0]
        hold = 0
        for price in prices:
            # print(price)
            if price <= lowest and hold == 0:
                lowest = price
                hold = 0
            elif price > previous:
                hold = 1
            elif price < previous and hold == 1:
                profits += previous - lowest
                lowest = price
                hold = 0
            elif price < previous and hold == 0:
                lowest = price
                hold = 0
            else:
                hold = 1
            # print('hold=', hold)
            # print('lowest=', lowest)
            previous = price
        if hold == 1:
            profits += prices[-1] - lowest
        # print(profits)
        return profits
