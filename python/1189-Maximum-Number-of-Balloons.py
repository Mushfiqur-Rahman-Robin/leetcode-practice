class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq_text = Counter(text)

        return min(freq_text['b'], freq_text['a'], freq_text['l'] // 2, \
                    freq_text['o'] // 2, freq_text['n'])
        

# tutorial link: https://www.youtube.com/watch?v=fVCBqMHwhww
# time complexity: O(n)
# space complexity: O(1)
