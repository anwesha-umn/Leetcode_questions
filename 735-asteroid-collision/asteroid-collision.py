class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 1
        n = len(asteroids)

        while i < n:

            if i > 0 and (asteroids[i] < 0 and asteroids[i-1] > 0):
                if abs(asteroids[i]) == abs(asteroids[i-1]):
                    asteroids.pop(i)
                    asteroids.pop(i-1)
                    i-=2
                
                elif abs(asteroids[i]) < abs(asteroids[i-1]):
                    asteroids.pop(i)
                    i -= 1

                else:
                    asteroids.pop(i-1)
                    i -= 1
                
                n = len(asteroids)
            else:
                i+=1

        return asteroids

                
        