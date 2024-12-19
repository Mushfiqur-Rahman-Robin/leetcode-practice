class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = Counter(s1)

        left = 0
        right = len(s1)

        while right <= len(s2):
            if Counter(s2[left: right]) != freq_s1:
                left += 1
                right += 1

            elif Counter(s2[left: right]) == freq_s1:
                return True
        
        return False

# tutorial link: https://www.youtube.com/watch?v=quSfR-uwkZU
# time complexity: O(|s1| × |s2|)
# space complexity: O(|s1|)
# this can be further optimized. check note for optimized version.
