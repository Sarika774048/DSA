# LeetCode 3492 - Maximum contaier on a ship

You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the deck can hold one container with a weight of exactly w.

However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, maxWeight.

Return the maximum number of containers that can be loaded onto the ship.
  
class Solution:
    def maxContainers(self, n: int, w: int, max_weight: int) -> int:
        max_possible = max_weight // w
        max_cells = n*n
        return min(max_possible, max_cells)
