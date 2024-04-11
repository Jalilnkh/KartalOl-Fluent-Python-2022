class solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_to_ind = {}
        for ind, val in enumerate(nums):

            comp = target - val
            if comp in num_to_ind:
                return [num_to_ind[comp], ind]
            
            num_to_ind[val] = ind

        return []
    
if __name__ == "__main__":
    int_list = [1, 3, 4, 6, 7, 11]
    target = 9

    sol = solution()
    print(sol.twoSum(int_list, target))
