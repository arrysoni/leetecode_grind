"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If no profit can be made, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transactions are done, so the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        print('The maximum profit is: ', max_profit)
        return max_profit


prices1 = [7, 1, 5, 3, 6, 4]
Solution().maxProfit(prices1)

prices2 = [7, 6, 4, 3, 1]
Solution().maxProfit(prices2)
