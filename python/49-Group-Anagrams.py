class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
            # print(key, ans[key], ans)
        
        return list(ans.values())

# Solution Details: https://leetcode.com/problems/group-anagrams/solutions/5641123/video-create-keys-for-group-of-strings-2-solutions

# Time complexity: O(m∗nlogn)
# Space complexity: O(mn)
