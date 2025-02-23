class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        else:
            primes = [1]*n
            primes[0] = primes[1] = 0

            i = 2
            while i*i < n:
                if primes[i]==1:
                    multiple = i*i
                    while multiple < n:
                        primes[multiple] = 0
                        multiple += i
                i+=1

            return sum(primes)