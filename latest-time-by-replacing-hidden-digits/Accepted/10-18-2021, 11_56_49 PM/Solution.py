// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits

class Solution:
    def maximumTime(self, time: str) -> str:
        time_fixed = list(time)

        if time_fixed[0] == '?':
            if time_fixed[1] == '?':
                time_fixed[0] = '2'
                time_fixed[1] = '3'
            elif int(time_fixed[1]) > 3:
                time_fixed[0] = '1'
            else:
                time_fixed[0] = '2'
        elif time_fixed[1] == '?':
            if time_fixed[0] == '2':
                time_fixed[1] = '3'
            else:
                time_fixed[1] = '9'
        if time_fixed[3] == '?':
            time_fixed[3] = '5'
        if time_fixed[4] == '?':
            time_fixed[4] = '9'
        return ''.join(time_fixed)