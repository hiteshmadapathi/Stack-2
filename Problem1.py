# Time Complexity --> O(N) where N is the length of Logs list
# Space Complexity --> O(N)
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        st = []
        result = [0 for i in range(n)]
        prev = 0
        for log in logs:
            strarr = log.split(':')
            id, action, curr = int(strarr[0]), strarr[1], int(strarr[2])
            
            if action=='start':
                if len(st)>0:
                    result[st[-1]] += curr-prev 
                st.append(id)
                prev = curr
            else:
                popped = st.pop()
                result[popped] += curr-prev+1 
                prev = curr + 1
        return result 
