class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_gas = 0
        curr_gas = 0
        start_index = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:           # need to check if we can reach at the index we began 
                start_index = i + 1    #  Update the start index to the next position
                curr_gas = 0            # Reset current gas to zero since we can't start from the previous start_index
        
        # if total gas is >=0  we can complete the circuit
        if total_gas >= 0:
            return start_index
        else:
            return -1
        