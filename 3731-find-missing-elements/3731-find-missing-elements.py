class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)
        sum = high - low + 1
        if sum == len(nums):
            return []
        else:
            temp = set(range(low,high))
            temp = list(temp - set(nums))
            return sorted(temp)