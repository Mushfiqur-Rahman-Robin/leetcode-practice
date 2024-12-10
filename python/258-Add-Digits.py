class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return (num % 9)

        # time complexity: O(1)
        # space complexity: O(1)

        # total = 0 

        # if num <= 9:
        #     return num

        # while num > 0:
        #     total += num % 10
        #     num = num // 10
        
        # return self.addDigits(total)

# tutorial link: https://www.youtube.com/watch?v=gPZvXaniFDQ
        
