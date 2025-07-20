class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res_dir = []
        set_dir = set(folder)

        for f in folder:
            res_dir.append(f)

            for i in range(len(f)):
                if f[i] == "/" and f[:i] in set_dir:
                    res_dir.pop()
                    break
        
        return res_dir
        
# Time Complexity: O(n⋅k)
# Space Complexity: O(n)
# Check note
