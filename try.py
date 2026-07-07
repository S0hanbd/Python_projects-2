

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}  # Map to store: value -> index
    print(seen)
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    print(seen)
    return None


print(twoSum([3, 2, 4], 6))  # Output: [1, 2]