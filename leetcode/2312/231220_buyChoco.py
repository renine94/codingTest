class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        min_val = sorted_prices.pop(0)
        if money > min_val:
            remain_money = money - min_val
        else:
            return money

        second_min_val = sorted_prices.pop(0)
        if remain_money > second_min_val:
            remain_money -= second_min_val
            return remain_money
        elif remain_money == second_min_val:
            return 0
        else:
            return money


########################################


class Solution:
    def buyChoco(self, prices, money):
        prices.sort()
        check_lists = prices[:2]
        target_price = sum(check_lists)
        remain_money = money - target_price
        if remain_money < 0:
            return money
        return remain_money
