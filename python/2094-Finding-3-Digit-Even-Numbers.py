from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        resulted_list = []
        three_digit_nums = permutations(digits, 3)
        
        for nums in three_digit_nums:
            if nums[0] != 0 and nums[-1] % 2 == 0:
                resulted_list.append(int(''.join(map(str, nums))))
        
        return sorted(set(resulted_list))


# time complexity: O(n^3)
# space complexity: O(n^3)


# To **optimize** the code, we can avoid using `itertools.permutations`, which generates **all 3-length permutations**, even invalid ones (like starting with `0` or ending in odd digits), and may produce duplicates if the input contains repeated digits.

# Instead, we’ll **manually generate valid 3-digit combinations**, which gives us more control and avoids overhead from `itertools`.

# ---

# ### ✅ Optimized Code (No `itertools`)

# ```python
# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         result = set()
#         n = len(digits)

#         for i in range(n):
#             for j in range(n):
#                 if j == i:
#                     continue
#                 for k in range(n):
#                     if k == i or k == j:
#                         continue

#                     # Form the number from digits[i], digits[j], digits[k]
#                     if digits[i] == 0:
#                         continue  # Skip if leading digit is 0
#                     if digits[k] % 2 != 0:
#                         continue  # Last digit must be even

#                     number = digits[i] * 100 + digits[j] * 10 + digits[k]
#                     result.add(number)

#         return sorted(result)
# ```

# ---

# ### 🔍 Why This Is More Efficient

# - Skips invalid permutations early (e.g., leading zero, odd last digit)
# - Avoids using `permutations()` which internally builds all possibilities
# - Uses **only `O(n³)`** loops directly, which is fast for small `n` (at most `6` or `7` for LeetCode constraints)
# - Uses a **set** to automatically deduplicate values

# ---

# ### ⏱ Time and Space Complexity

# | Metric           | Value           |
# |------------------|-----------------|
# | **Time**         | `O(n³)`         |
# | **Space**        | `O(k)`          |

# - `n` is the number of digits
# - `k` is the number of unique 3-digit even numbers (at most `900`, from 100 to 998)

# ---
