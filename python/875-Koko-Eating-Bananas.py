class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            hours = 0 

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res

# tutorial link: https://www.youtube.com/watch?v=U2SozAs9RzA
# time complexity: O(n.log(max(piles)))
# space complexity: O(1)
# check note
