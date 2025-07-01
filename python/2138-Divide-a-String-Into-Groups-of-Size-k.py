class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = []

        remainder = len(s) % k
        if remainder != 0:
            s += fill * (k - remainder)
        
        for i in range(0, len(s), k):
            arr.append(s[i:i+k])

        return arr 

# time complexity: O(n)
# space complexity: O(n)
