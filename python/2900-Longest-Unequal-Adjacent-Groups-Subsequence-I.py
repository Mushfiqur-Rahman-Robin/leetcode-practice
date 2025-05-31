class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result_list = []
        first_elem = words[0]
        result_list.append(first_elem)

        for i in range(len(groups) - 1):
            if groups[i] != groups[i+1]:
                result_list.append(words[i+1])

        return result_list

# time complexity: O(n)
# space complexity: O(n)
