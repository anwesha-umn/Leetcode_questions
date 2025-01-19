class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        altitudes = [0, gain[0]]

        diff = gain[0]

        for i in range(len(gain)-1):

            diff += gain[i+1]

            altitudes.append(diff)

        return max(altitudes)