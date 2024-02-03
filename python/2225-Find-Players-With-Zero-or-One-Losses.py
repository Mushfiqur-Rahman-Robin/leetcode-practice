class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        not_lost_any = set()
        lost_one = []

        winners = set()
        loosers = []

        for elem in matches:
            winners.add(elem[0])
            loosers.append(elem[1])

        not_lost_any = winners - set(loosers)

        looser_freq = Counter(loosers)
        
        for key, val in looser_freq.items():
            if val == 1:
                lost_one.append(key)

        return [sorted(list(not_lost_any)), sorted(list(lost_one))]
