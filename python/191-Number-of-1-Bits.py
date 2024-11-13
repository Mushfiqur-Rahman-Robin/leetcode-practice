class Solution:
    def hammingWeight(self, n: int) -> int:
        convert_to_bin = bin(n)[2:]
        total_set_bit = sum(1 for c in convert_to_bin if c == '1')
        
        return total_set_bit

        # res = 0 # Another solution

        # for i in range(32):
        #     if (n >> i) & 1:
        #         res += 1

        # return res
        
