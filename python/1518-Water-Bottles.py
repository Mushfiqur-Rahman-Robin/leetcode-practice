class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        extra_bottles = 0
        temp_numbottles = numBottles

        while (temp_numbottles >= numExchange): # this loop accounts for getting the number of extra bottles
            extra_bottles += temp_numbottles // numExchange
            temp_numbottles = (temp_numbottles // numExchange) + temp_numbottles % numExchange
        
        return numBottles + extra_bottles
        

# Time Complexity: O(numBottles / numExchange) because in each iteration you reduce bottles roughly by a factor of numExchange.
# Space Complexity: O(1) → only a few variables.
# Check Note
