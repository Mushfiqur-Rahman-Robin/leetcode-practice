class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_of_numbers = Counter(nums)

        top_k_frequent = frequency_of_numbers.most_common(k)

        top_k = []
        for elem in top_k_frequent:
            top_k.append(elem[0])

        return top_k


# Time complexity: O(n log k) 
# Space complexity: O(n)
