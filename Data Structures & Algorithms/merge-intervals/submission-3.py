class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])

        ret=[]

        ret.append(intervals[0])

        for start, end in intervals[1:]:
            if start<=ret[-1][1]:
                ret[-1][1]=max(end, ret[-1][1])
            else:
                ret.append([start, end])

        return ret