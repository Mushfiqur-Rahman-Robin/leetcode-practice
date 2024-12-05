class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # traditional solution
        i = len(digits) - 1

        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            
            i -= 1
        
        return [1] + digits

        # tutorial link: https://www.youtube.com/watch?v=jIaA8boiG1s
        # time complexity: O(n)
        # space complexity: O(n)
        # check note


        # hacky solution
        # number = ""

        # for n in digits:
        #     number += str(n)

        # tmp_number = str(int(number) + 1)
        # res = [0] * len(tmp_number)

        # for i in range(len(tmp_number)):
        #     res[i] = int(tmp_number[i])
        
        # return res

        # time complexity: O(n)
        # space complexity: O(n)   
