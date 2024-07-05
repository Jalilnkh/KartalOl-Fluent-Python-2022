from typing import List

class Solution:
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroid_collision([5,10,-5]))
