class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for battery_percent in batteryPercentages:
            if battery_percent - tested > 0:
                tested += 1
        return tested

        
