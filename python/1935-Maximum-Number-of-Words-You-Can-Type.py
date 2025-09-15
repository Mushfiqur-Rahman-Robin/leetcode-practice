class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cant_type_count = 0
        unique_broken = set(brokenLetters)
        words = text.split(" ")

        for w in words:
            for letter in unique_broken:
                if letter in w:
                    cant_type_count += 1
                    break
        
        return len(words) - cant_type_count

# time complexity: O(n^2)
# space complexity: O(n)
