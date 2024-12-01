class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # more optimized version
        seen = set()

        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        
        return False

        # time complexity: O(n)
        # space complexity: O(n)


        # unoptimized version
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if i != j and arr[i] == 2 * arr[j]:
        #             return True

        # return False

        # time complexity: O(n^2)
        # space complexity: O(n)
