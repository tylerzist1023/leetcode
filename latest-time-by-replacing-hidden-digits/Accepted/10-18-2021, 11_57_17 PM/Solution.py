// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits

class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == '?':
            try:
                if int(time[1]) > 3:
                    time = time[:0] + '1' + time[1:]
                else:
                    time = time[:0] + '2' + time[1:]
            except:
                time = time[:0] + '2' + time[1:]
        if time[1] == '?':
            if time[0] == '2':
                time = time[:1] + '3' + time[2:]
            else:
                time = time[:1] + '9' + time[2:]
        if time[3] == '?':
            time = time[:3] + '5' + time[4:]
        if time[4] == '?':
            time = time[:4] + '9' + time[5:]
        return time