class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res =  ""
        # chars = zip(*strs)

        # for c in chars:
        #     if len(set(c)) == 1:
        #         res += c[0]
        #     else:
        #         break

        # return res

        # Eg: chars = zip('flower', 'flow', 'flight')
        # chars = [(f, f, f), (l, l, l), (o, o, i), (w, w, g)]

        # Then we are just iterating this chars list and checking if all elements are same:
        # len(set(char)) == 1

        # If it is, we add char to res else break as soon as we find the first mismatch

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s[i]

        return res

# tutorial link: https://www.youtube.com/watch?v=0sWShKIJoo4
# check note 
