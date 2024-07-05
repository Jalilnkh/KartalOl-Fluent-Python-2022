from typing import List

class Solution:
    def largest_altitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        
        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        
        return max_altitude


if __name__ == "__main__":
    sol = Solution()
    print(sol.largest_altitude([-5,1,5,0,-7]))
