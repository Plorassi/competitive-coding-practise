class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ans = 0
        res = {position[i]:speed[i] for i in range(len(position))}
        position.sort()
        
        time = 0
        for i in range(len(position))[::-1]:
            tmp = (target - position[i])/res[position[i]]
            if tmp > time:
                ans += 1
                time = tmp
                
        return ans
