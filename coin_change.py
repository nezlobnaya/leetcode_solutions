"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""


from typing import List
# Option 1 using deque
# from collections import deque
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         my_queue = deque([(amount, 0)])
#         already_checked = set([])
#         while my_queue:
#             amount, level = my_queue.popleft()
#             if amount == 0:
#                 return level
#             for coin in coins:
#                 diff = amount - coin
#                 if diff >= 0 and diff not in already_checked:
#                     already_checked.add(diff)
#                     my_queue.append((diff, level + 1))
#         return -1 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # num_of_coins = [0] + [-1] * amount

        # for index in range(amount):
        #     if num_of_coins[index] < 0:
        #         continue
        #     for coin in coins:
        #         if index + coin > amount:
        #             continue
        #         if num_of_coins[index + coin] < 0 or num_of_coins[index + coin] > num_of_coins[index] + 1:
        #             num_of_coins[index + coin] = num_of_coins[index] + 1
        # return num_of_coins[amount]

        # num_of_coins = [0] + [float("inf")] * amount
        # for coin in coins:
        #     for value in range(len(num_of_coins)):
        #         if coin <= value:
        #             num_of_coins[value]= min(num_of_coins[value], 1 +num_of_coins[value-coin])
        # return num_of_coins[amount] if num_of_coins[amount] != float("inf") else -1
                               
        num_of_coins = [0] + [float('inf')] * (amount)

        for coin in coins:
            for index in range(coin, amount + 1):
                num_of_coins[index] = min(num_of_coins[index], num_of_coins[index - coin] + 1)
        return num_of_coins[amount] if num_of_coins[amount] != float('inf') else -1 



print(Solution().coinChange([1,2,5], 11))

