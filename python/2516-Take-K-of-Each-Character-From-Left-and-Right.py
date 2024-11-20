class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_char_count = Counter(s)

        if total_char_count['a'] < k or total_char_count['b'] < k or total_char_count['c'] < k:
            return -1

        # Required minimum counts after removing a valid middle segment
        required_a = total_char_count['a'] - k
        required_b = total_char_count['b'] - k
        required_c = total_char_count['c'] - k

        l = 0
        current_char_count = Counter()
        max_middle_length = 0

        for r in range(len(s)):
            current_char_count[s[r]] += 1

            # Shrink the window if the counts exceed the required limits
            while (
                current_char_count['a'] > required_a or
                current_char_count['b'] > required_b or
                current_char_count['c'] > required_c
            ):
                current_char_count[s[l]] -= 1
                l += 1

            max_middle_length = max(max_middle_length, r - l + 1)

        return len(s) - max_middle_length
