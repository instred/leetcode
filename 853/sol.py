from typing import List
from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = {a : b for a,b in zip(position,speed)}
        position.sort(reverse=True)
        for p in position:
            steps = (target-p) / cars[p]
            stack.append(steps)
            if len(stack) >=2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)




if __name__ == "__main__":
    sol = Solution()
    target = 12;position = [10,8,0,5,3]; speed = [2,4,1,1,3]
    target2 = 10; position2 = [3]; speed2 = [3]
    target3 = 100; position3 = [0,2,4]; speed3 = [4,2,1]
    target4 = 10; position4 = [0,4,2]; speed4 = [2,1,3]
    print(sol.carFleet(target, position, speed))
    print(sol.carFleet(target2, position2, speed2))
    print(sol.carFleet(target3, position3, speed3))
    print(sol.carFleet(target4, position4, speed4))