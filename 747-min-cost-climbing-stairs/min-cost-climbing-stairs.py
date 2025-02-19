class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        # curr_cost = 0
        # total_cost = 0
        
        # if cost[0] < cost[1] and cost[2] < cost[1]:
        #     start = 0
        # elif cost[0] < cost[1] and cost[1] < cost[2]:
        #     start = 0
        # else:
        #     start = 1

        # total_cost = cost[start]

        # i = start

        # while i < len(cost) - 2:
        #     if (cost[i] <= cost[i+1] and cost[i+2] <= cost[i+1]) or (cost[i] < cost[i+1] and cost[i+1] < cost[i+2]):
        #         i+=2
        #     else:
        #         i+=1
        #     total_cost += cost[i]

        # return total_cost
        cost.append(0) # top [10,15,20,0]
        
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])

            

            