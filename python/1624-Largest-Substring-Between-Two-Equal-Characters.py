class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = -1

        # first_index = {}

        # for i in range(len(s)):
        #     if s[i] in first_index:
        #         count = max(count, i - first_index[s[i]]-1)
        #     else:
        #         first_index[s[i]] = i
        # return count

        for start in range(len(s)):
            for next_elem in range(start, len(s)):
                if s[start] == s[next_elem]:
                    count = max(count, next_elem - start - 1)
        
        return count
        
        
