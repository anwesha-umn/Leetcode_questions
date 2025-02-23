class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        else:
            primes = [True] * n
            primes[0] = primes[1] = False


            i = 2

            while i*i < n:
                if primes[i]:
                    multiple = i * i

                    while multiple < n:
                        primes[multiple] = False
                        multiple += i
                i+=1

            count = 0
            for cond in primes:
                if cond==True:
                    count+=1
            
            return count
        