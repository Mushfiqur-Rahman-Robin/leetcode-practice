class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        res = ""
        m = len(word) - numFriends + 1

        if numFriends == 1:
            return word

        for i in range(len(word)):
            res = max(res, word[i:i+m])
        
        return res

# time complexity: O(n^2)
# space complexity: O(n)
