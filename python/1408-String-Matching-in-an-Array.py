class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # brute force
        res = set()

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j] in words[i]:
                    res.add(words[j])
                elif words[i] in words[j]:
                    res.add(words[i])

        return list(res)

# time complexity: O(n^2)
# space complexity: O(n)  
# check note for optimized approach
