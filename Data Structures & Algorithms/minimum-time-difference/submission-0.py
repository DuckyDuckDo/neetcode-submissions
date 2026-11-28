class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timePoints.append(timePoints[0])
        print(timePoints)
        def get_difference(time1, time2):
            t1_hr, t1_min = [int(x) for x in time1.split(':')]
            t2_hr, t2_min = [int(x) for x in time2.split(':')]

            carry = 0
            if t2_min > t1_min:
                carry = 1
                min_difference = t2_min + 60 - t1_min
            
            else:
                min_difference = t2_min - t1_min
            
            if t2_hr > t1_hr:
                hr_difference = t2_hr + 24 - t1_hr - carry
            
            else:
                hr_difference = t2_hr - t1_hr - carry

            return (hr_difference * 60 + min_difference) % 1440

        res = float('inf')

        for i in range(len(timePoints) - 1):
            if timePoints[i] == timePoints[i + 1]:
                return 0
            res = min(res, get_difference(timePoints[i], timePoints[i+1]))
        
        return res
