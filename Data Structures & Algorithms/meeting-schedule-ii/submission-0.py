"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        (0,40),(5,10),(15,20)

        sort by start (0,40),(5,10),(15,20)

        sort by end (5,10),(15,20),(0,40)
        '''

        start=[]
        end=[]

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        '''
        start=[0, 5, 15]
        end=[10, 20, 40]

        '''

        count=0
        max_rooms=0

        s,e=0,0

        while s<len(start):
            if start[s]<end[e]:
                count+=1
                s+=1
                max_rooms=max(max_rooms, count)
            else:
                count-=1
                e+=1
            
        return max_rooms





        

