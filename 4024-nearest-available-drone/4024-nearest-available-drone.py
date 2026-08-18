class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min = 99999
        res = -1
        for i, drone in enumerate(drones):
            distance = abs(drone[0] - target[0]) + abs(drone[1] - target[1])
            if distance <= drone[2] and min>abs(distance):
                min = distance
                res = i
        return res