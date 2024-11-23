class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])

        for row in box:
            empty_index = len(row) - 1
            for i in range(len(row) - 1, -1, -1):
                if row[i] == "#":
                    row[i], row[empty_index] = row[empty_index], row[i]
                    empty_index -= 1
                elif row[i] == '*':
                    empty_index = i - 1

        rotated_box = [[None] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated_box[j][rows - 1 - i] = box[i][j]
        
        return rotated_box


# theory link: https://www.youtube.com/watch?v=LZr1w0LVzFw
# time complexity: O(m*n)
# space complexity: O(m*n)
# check note
        
        
