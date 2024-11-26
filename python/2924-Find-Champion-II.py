class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming_edge_count = [0] * n
        champion = []

        for src, dst in edges:
            incoming_edge_count[dst] += 1
        
        for i, incoming_cnt in enumerate(incoming_edge_count):
            if incoming_cnt == 0:
                champion.append(i)
            
        return -1 if len(champion) > 1 else champion[0]
        

# tutorial link: https://www.youtube.com/watch?v=HjSmSLPR7S4
# time complexity: O(E+V)
# space complexity: O(V)
# check note
