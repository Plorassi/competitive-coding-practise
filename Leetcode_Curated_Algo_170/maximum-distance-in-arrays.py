class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        first_max = [float('-inf'),-1]
        second_min = 0
        for i in range(len(arrays)):
            if arrays[i][-1] > first_max[0]:
                first_max[0] = arrays[i][-1]
                first_max[1] = i
                second_min = arrays[i][0]

        second_max = float('-inf')
        first_min = float('inf')
        for i in range(len(arrays)):
            if i != first_max[1]:
                if arrays[i][-1] > second_max:
                    second_max = arrays[i][-1]
                if arrays[i][0] < first_min:
                    first_min = arrays[i][0]

        return max(abs(first_max[0]-first_min), abs(second_max-second_min))


        
