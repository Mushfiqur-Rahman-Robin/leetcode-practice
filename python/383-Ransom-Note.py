class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hashmap = {}

        for char in magazine:
            magazine_hashmap[char] = 1 + magazine_hashmap.get(char, 0)

        for char in ransomNote:
            if char not in magazine_hashmap or magazine_hashmap[char] == 0:
                return False
            
            magazine_hashmap[char] -= 1
        
        return True

# time complexity: O(k∗(m+n)), where k is the number of unique characters in ransomNote. m is the length of magazine. n is the length of ransomNote.
# space complexity: O(26) -> O(1)
