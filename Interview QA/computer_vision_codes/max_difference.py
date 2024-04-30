def max_difference_pair(nums):
    if len(nums) < 2:
        return None, None, None  # No valid pair

    min_value = nums[0]
    max_diff = float('-inf')
    best_pair = None

    for i in range(1, len(nums)):
        current_diff = nums[i] - min_value

        if current_diff > max_diff:
            max_diff = current_diff
            best_pair = (min_value, nums[i])
        
        if nums[i] < min_value:
            min_value = nums[i]

    if best_pair:
        return best_pair[0], best_pair[1], max_diff
    else:
        return None, None, None  # No valid pair

# Example usage
nums = [3, 5, 2, 7, 1, 8, 4, 10]
num1, num2, difference = max_difference_pair(nums)
if num1 is not None:
    print(f"Pair: ({num1}, {num2}) with maximum difference: {difference}")
else:
    print("No valid pair found.")
