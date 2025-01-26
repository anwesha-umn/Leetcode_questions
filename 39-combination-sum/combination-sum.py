class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        total = 0
        res = []

        def decision_tree(index, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if total > target or index >= len(candidates):
                return 

            # first number include case
            comb.append(candidates[index])
            # add the same index no. again
            decision_tree(index, comb, total + candidates[index])

            # second: number exclude case
            comb.pop()
            # increment index to next
            decision_tree(index + 1, comb, total)

            return res

        return decision_tree(0, [], 0)


        