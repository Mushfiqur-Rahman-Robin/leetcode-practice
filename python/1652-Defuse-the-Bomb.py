class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        if k == 0:
            return result

        if k > 0:
            window_sum = sum(code[1:k+1])
            for i in range(n):
                result[i] = window_sum
                window_sum += code[(i + k + 1) % n] - code[(i + 1) % n]
        else:
            k = -k
            window_sum = sum(code[-k:])
            for i in range(n):
                result[i] = window_sum
                window_sum += code[i] - code[(i - k) % n]
        
        return result

# tutorial link: https://www.youtube.com/watch?v=c4oOIi5YTE4

# check note
