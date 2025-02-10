# https://leetcode.com/problems/fizz-buzz/

# Flutter Daily Practice
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
                if i % 15 == 0:
                     result.append("FizzBuzz")
                elif i % 3 == 0:
                    result.append("Fizz")
                elif i % 5 == 0:
                    result.append("Buzz")
                else:
                    result.append(str(i))
        return result
solution=Solution()
result=solution.fizzBuzz(4)
print(result)
