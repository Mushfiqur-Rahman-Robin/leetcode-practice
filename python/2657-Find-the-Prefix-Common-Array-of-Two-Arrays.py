class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = [0] * len(A)
        common_count = 0
        seen = set()

        for i in range(0, len(A)):
            if A[i] in seen:
                common_count += 1
            seen.add(A[i])

            if B[i] in seen:
                common_count += 1
            seen.add(B[i])

            res[i] = common_count

        return res            

# time complexity: O(n)
# space complexity: O(n)
# check note
