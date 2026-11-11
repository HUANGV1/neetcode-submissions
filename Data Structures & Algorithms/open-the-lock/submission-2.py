class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        

        deadends_set=set(deadends)

        if '0000' in deadends_set: return -1

        q=deque()

        q.append('0000')
        seen={'0000'}

        def bolu(number):
            # list all 8 possible results
            ret=set()
            for i in range(len(target)):
                up = (int(number[i])+1)%10
                up_num=number[:i]+str(up)+number[i+1:]
                down = (int(number[i])-1)%10
                down_num=number[:i]+str(down)+number[i+1:]

                ret.add(up_num)
                ret.add(down_num)
            return ret
  

        turns=0
        while q:
            for _ in range(len(q)):
                current=q.popleft()
                if current==target:
                    return turns
                
                options=bolu(current)

                for option in options:
                    if option in deadends_set or option in seen:
                        continue
                    q.append(option)
                    seen.add(option)
            turns+=1

        return -1
        
