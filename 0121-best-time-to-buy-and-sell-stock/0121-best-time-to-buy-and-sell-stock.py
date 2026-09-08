class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        m_p=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            p=m_p-prices[i]
            if p>max_profit:
                max_profit=p
            if prices[i]>m_p:
                m_p=prices[i]
        return max_profit
            