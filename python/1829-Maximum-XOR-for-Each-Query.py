class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        answer = []
        mask = (1 << maximumBit) - 1

        for n in nums:
            xor ^= n

        for n in reversed(nums):
            answer.append(xor ^ mask)
            xor ^= n

        return answer


# Time complexity: O(n)
# Space complexity: O(1)
# Tutorial link: https://www.youtube.com/watch?v=FlSS5reeFyE
