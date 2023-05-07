class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        prev_row = costs[0]

        for i in range(1,len(costs)):
            min_val = min(prev_row)
            min_val_index = prev_row.index(min_val)

            second_val = min(prev_row[:min_val_index]+prev_row[min_val_index+1:])

            for j in range(len(costs[0])):
                costs[i][j] += min_val if j != min_val_index else second_val

            prev_row = costs[i]

        return min(costs[-1])
        
