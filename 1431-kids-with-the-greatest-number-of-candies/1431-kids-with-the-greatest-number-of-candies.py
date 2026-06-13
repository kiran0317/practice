class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        res = []
        for i in candies:
            res.append( True if i+extraCandies>=max_ else False)
        return res