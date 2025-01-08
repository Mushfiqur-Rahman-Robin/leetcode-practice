class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        total_prefix_suffix_count = 0

        def isPrefixAndSuffix(wordi, wordj):
            len_wordi = len(wordi)

            if len(wordi) > len(wordj):
                return False
            
            return wordj[:len_wordi] == wordi and wordj[-len_wordi:] == wordi

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    total_prefix_suffix_count += 1
        
        return total_prefix_suffix_count


        # another solution
        # count = 0

        # for i in range(len(words)):
        #     for j in range(i + 1, len(words)):
        #         if words[j].startswith(words[i]) and words[j].endswith(words[i]):
        #             count += 1

        # return count

    
# time complexity: O(n^2 * m)
# space complexity: O(1)
        
