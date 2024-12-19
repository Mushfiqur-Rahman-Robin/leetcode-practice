class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # optimized version
        merged = []

        for a, b in zip(word1, word2):
            merged.append(a + b)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)

        # time complexity: o(m+n)
        # space complexity: O(m+n)

        # initial version
        # min_word_len = min(len(word1), len(word2))
        # max_word_len = max(len(word1), len(word2))
        # res_str = ""
        # additional_str = ""

        # if len(word1) > len(word2):
        #     additional_str += word1[min_word_len:]
        # if len(word2) > len(word1):
        #     additional_str += word2[min_word_len:]

        # for i, j in zip(word1, word2):
        #     res_str = res_str + i + j

        # return res_str + additional_str

        # time complexity: O(k^2)
        # space complexity: O(m+n)
