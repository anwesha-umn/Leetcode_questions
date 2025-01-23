class Solution {
public:
    int countPrimes(int n) {

        if (n<2) return 0;
        // marking all multiples from 2 to n as non-prime
        int cnt = 0;

        vector<bool>primes(n, true); // first mark all numbers as false
        primes[0] = primes[1] = false;
        
        for (int i=2; i*i < n; ++i){
            if (primes[i]) {
                // mark multples of i as non prime
                for (int multiple = i*i; multiple < n; multiple+=i){
                    primes[multiple] = false;
                }
            }
        }
        // count the no. of true values
        cnt = count(primes.begin(), primes.end(), true);
        return cnt;
    }
};

