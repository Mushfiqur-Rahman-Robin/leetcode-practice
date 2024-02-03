class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x , y = 0, 0
        visited = {(0, 0)}

        for elem in path:
            if elem == 'N':
                y += 1
            elif elem == 'S':
                y -= 1
            elif elem == 'W':
                x -= 1
            elif elem == 'E':
                x += 1
            
            position = (x , y)
            
            if position in visited:
                return True

            visited.add(position)

        return False
