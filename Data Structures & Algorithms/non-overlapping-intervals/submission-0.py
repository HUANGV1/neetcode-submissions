class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        idea is that when two are overlapping, we want to remove the one that ends later (greedy) to decrease chance of overlapping with later intervals
        '''

        intervals.sort() # sort by the start time

        removes=0

        prevEnd=intervals[0][1]

        for start, end in intervals[1:]:
            if start<prevEnd:
                removes+=1
                prevEnd=min(end, prevEnd)
            else:
                prevEnd=end

        return removes
