def maxProfit(self, prices):
    # for all possible transactions coming after global minimum, global minimum is the right buy for all sells coming afterwards
    # for all possible transactions coming before global minimum, the second global minimum is the right buy for all sells coming between all sells after & all buys before
    # for all possible transactions coming before the second-best minimum, the third-best global minimum is the right buy for all sells coming between them
    # therefore, I just need to track the minimum seen so far, and the maximum profit I can get from the minimum seen so far
    if len(prices) == 0:
        return 0
    max_profit = 0
    min_buy = prices[0]
    
    for price in prices:
        if min_buy > price:
            min_buy = price
        else:
            max_profit = max(max_profit, price - min_buy)
    return max_profit