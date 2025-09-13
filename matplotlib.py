#include <bits/stdc++.h>
using namespace std;

static constexpr int MOD = 1e9+7, BASE30 = (1<<30) % MOD;

class Solution {
public:
    // ---------- Modular Arithmetic ----------
    static int modPow(long long base, int exponent) {
        if (exponent == 0) return 1;
        long long multiplier = (exponent & 1) ? base : 1;
        return modPow(base * base % MOD, exponent >> 1) * multiplier % MOD;
    }

    static int pow2mod(int exponent) {
        if (exponent < 30) return 1 << exponent;
        auto [quotient, remainder] = div(exponent, 30);
        long long basePart = modPow(BASE30, quotient);
        return basePart * (1 << remainder) % MOD;
    }

    static int modInverse(int x) {
        return modPow(x, MOD - 2); // Fermat's little theorem (works since MOD is prime)
    }

    // nCr % MOD using factorial + modular inverse
    static int nCrMod(int n, int r) {
        if (r < 0 || r > n) return 0;
        static vector<int> fact(1, 1), invFact(1, 1);
        static int computed = 0;
        if (n > computed) {
            for (int i = computed + 1; i <= n; i++) {
                fact.push_back(1LL * fact.back() * i % MOD);
            }
            invFact.resize(n + 1);
            invFact[n] = modInverse(fact[n]);
            for (int i = n; i > computed; i--) {
                invFact[i-1] = 1LL * invFact[i] * i % MOD;
            }
            computed = n;
        }
        return 1LL * fact[n] * invFact[r] % MOD * invFact[n-r] % MOD;
    }

    // ---------- Bit / Number utilities ----------
    static int countSetBits(int number) {
        int count = 0;
        while (number) {
            number &= (number - 1);
            count++;
        }
        return count;
    }

    static string toBinaryString(int number) {
        string result;
        for (int i = 29; i >= 0; i--)
            result.push_back((number & (1 << i)) ? '1' : '0');
        return result;
    }

    // ---------- XOR / Prefix ----------
    static int rangeXor(int l, int r) {
        return prefixXor(r) ^ prefixXor(l - 1);
    }

    static vector<long long> prefixSum(const vector<int>& arr) {
        vector<long long> pref(arr.size());
        partial_sum(arr.begin(), arr.end(), pref.begin());
        return pref;
    }

    // ---------- GCD / LCM ----------
    static int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }

    static long long lcm(int a, int b) {
        return (1LL * a * b) / gcd(a, b);
    }

    static int gcdArray(const vector<int>& arr) {
        return accumulate(arr.begin(), arr.end(), arr[0], gcd);
    }

    static long long lcmArray(const vector<int>& arr) {
        return accumulate(arr.begin()+1, arr.end(), (long long)arr[0], 
            [](long long a, int b){ return (a / gcd(a,b)) * b; });
    }

    // ---------- Primes ----------
    static bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    static vector<int> sieve(int n) {
        vector<bool> isPrime(n+1, true);
        vector<int> primes;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
                for (long long j = 1LL*i*i; j <= n; j += i) isPrime[j] = false;
            }
        }
        return primes;
    }

    // ---------- Fibonacci / Factorial ----------
    static int factorialMod(int n) {
        long long result = 1;
        for (int i = 2; i <= n; i++) {
            result = (result * i) % MOD;
        }
        return result;
    }

    static int fibonacciMod(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        long long a = 0, b = 1, c;
        for (int i = 2; i <= n; i++) {
            c = (a + b) % MOD;
            a = b;
            b = c;
        }
        return b;
    }

    // Matrix exponentiation for Fibonacci / Recurrence
    static vector<vector<int>> matrixMultiply(const vector<vector<int>>& A, const vector<vector<int>>& B) {
        int n = A.size();
        vector<vector<int>> C(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < n; j++) {
                    C[i][j] = (C[i][j] + 1LL*A[i][k]*B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    static vector<vector<int>> matrixPower(vector<vector<int>> base, int exp) {
        int n = base.size();
        vector<vector<int>> result(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) result[i][i] = 1;
        while (exp > 0) {
            if (exp & 1) result = matrixMultiply(result, base);
            base = matrixMultiply(base, base);
            exp >>= 1;
        }
        return result;
    }

    // ---------- Extra Helpers ----------
    static bool isPalindromeString(const string& s) {
        return equal(s.begin(), s.begin() + s.size()/2, s.rbegin());
    }

    static bool isPalindromeNumber(int x) {
        string s = to_string(x);
        return isPalindromeString(s);
    }

    static int intSqrt(int x) {
        int r = sqrt(x);
        while ((long long)(r+1)*(r+1) <= x) r++;
        while ((long long)r*r > x) r--;
        return r;
    }

private:
    // Helper for rangeXor
    static int prefixXor(int x) {
        switch (x & 3) {
            case 0: return x;
            case 1: return 1;
            case 2: return x + 1;
            case 3: return 0;
        }
        return 0;
    }
};
