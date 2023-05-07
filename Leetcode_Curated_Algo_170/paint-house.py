class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        for i in range(1,len(costs)):

            first_min = min(costs[i-1])
            first_min_index = costs[i-1].index(first_min)
            second_min = min(costs[i-1][:first_min_index]+costs[i-1][first_min_index+1:])

            #print(first_min, first_min_index, second_min)

            for j in range(len(costs[0])):
                if j == first_min_index:
                    costs[i][j] += second_min
                else:
                    costs[i][j] += first_min

            #print(first_min_index, second_min, costs[i])

        return min(costs[-1]) 
