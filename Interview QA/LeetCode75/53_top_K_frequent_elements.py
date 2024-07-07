from typing import List
class Solution:
    def top_K_frequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        # Step 2: Sort elements by frequency
        frequency_list = list(frequency_dict.items())
        frequency_list.sort(key=lambda x: x[1], reverse=True)
        
        # Step 3: Extract the top k elements
        result = []
        for i in range(k):
            result.append(frequency_list[i][0])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.top_K_frequent([1,1,1,2,2,3], 2))
