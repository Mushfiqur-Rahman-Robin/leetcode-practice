class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sub = nums[0]

        for n in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += n

            max_sub = max(max_sub, current_sum)      

        return max_sub  

# https://www.youtube.com/watch?v=5WZl3MMT0Eg

# Time complexity O(n)
# Space Complexity O(n)

Kadane's algorithm is an efficient way to find the maximum sum subarray from a given array of integers. This subarray can consist of contiguous elements. The beauty of Kadane's algorithm lies in its simplicity and elegance, which allows it to run in linear time, making it an 

O(n) algorithm, where n is the number of elements in the array.

How Kadane's Algorithm Works
The algorithm initializes two variables: one to store the maximum sum found so far (initially set to the first element of the array or zero if you're considering empty subarrays as well) and another to store the current sum as it iterates through the array.

As it traverses the array from left to right, it adds the current element to the current sum. If at any point the current sum becomes negative, the algorithm resets the current sum to zero (or keeps it as the current element if not considering empty subarrays) because a negative sum will not contribute to a maximum sum of a future subarray. If the current sum is greater than the maximum sum found so far, the algorithm updates the maximum sum with the current sum's value.


Kadane's algorithm is not just limited to finding the maximum sum in a subarray; with slight modifications, it can also be used to solve various other array-related problems, making it a versatile tool in the algorithm toolbox.

