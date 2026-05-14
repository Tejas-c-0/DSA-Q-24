nums = [23,2,4,6,7]
k = 6
def checkSubarraySum(nums, k):
    prefix_sum = 0
    seen = {0: -1}  # Initialize with prefix sum 0 at index -1

    for i, num in enumerate(nums):
        prefix_sum += num
        mod_value = prefix_sum % k

        if mod_value in seen:
            if i - seen[mod_value] > 1:  # Check for subarray length > 1
                return True
        else:
            seen[mod_value] = i

    return False