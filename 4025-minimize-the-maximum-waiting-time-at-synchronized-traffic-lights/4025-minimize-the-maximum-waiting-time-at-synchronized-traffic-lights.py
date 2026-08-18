class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        ans = 0
        g = max(lights)
        for arr in arrivalTime:
            r = arr%period
            if r>=g:
                ans = max(ans, period-r)
        return ans