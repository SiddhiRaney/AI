#include <bits/stdc++.h>
using namespace std;

static constexpr int MOD = 1e9+7, BASE30 = (1<<30) % MOD;

class Solution {
public:
    // Fast modular exponentiation
    static int modPow(long long base, int exponent) {
        if (exponent == 0) return 1;
        long long multiplier = (exponent & 1) ? base : 1;
        return modPow(base * base % MOD, exponent >> 1) * multiplier % MOD;
    }

    // Compute 2^exponent % MOD efficiently
    static int pow2mod(int exponent) {
        if (exponent < 30) return 1 << exponent;
        auto [quotient, remainder] = div(exponent, 30);
        long long basePart = modPow(BASE30, quotient);
        return basePart * (1 << remainder) % MOD;
    }

    // Original problem: product of powers of 2 for query ranges
    static vector<int> productQueries(int number, vector<vector<int>>& queries) {
        const int queryCount = queries.size();
        bitset<30> bits(number);
        vector<int> exponents;

        for (int bitIndex = 0; bitIndex < 30; bitIndex++)
            if (bits[bitIndex]) exponents.push_back(bitIndex);

        partial_sum(exponents.cbegin(), exponents.cend(), exponents.begin());

        vector<int> results(queryCount);
        for (int i = 0; i < queryCount; i++) {
            const int start = queries[i][0], end = queries[i][1];
            const int totalExp = exponents[end] - ((start == 0) ? 0 : exponents[start - 1]);
            results[i] = pow2mod(totalExp);
        }
        return results;
    }

    // Count set bits in a number (Brian Kernighan's Algorithm)
    static int countSetBits(int number) {
        int count = 0;
        while (number) {
            number &= (number - 1);
            count++;
        }
        return count;
    }

    // Convert integer to binary string representation
    static string toBinaryString(int number) {
        string result;
        for (int i = 29; i >= 0; i--)
            result.push_back((number & (1 << i)) ? '1' : '0');
        return result;
    }

    // Compute prefix XOR for a range [l, r]
    static int rangeXor(int l, int r) {
        return prefixXor(r) ^ prefixXor(l - 1);
    }

    // GCD using Euclidean algorithm
    static int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }

    // LCM using GCD
    static long long lcm(int a, int b) {
        return (1LL * a * b) / gcd(a, b);
    }

    // Factorial mod
    static int factorialMod(int n) {
        long long result = 1;
        for (int i = 2; i <= n; i++) {
            result = (result * i) % MOD;
        }
        return result;
    }

    // Check if a number is prime
    static bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    // Fibonacci mod
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

    // Prefix sum for an array
    static vector<long long> prefixSum(const vector<int>& arr) {
        vector<long long> pref(arr.size());
        partial_sum(arr.begin(), arr.end(), pref.begin());
        return pref;
    }

private:
    // Helper for rangeXor
    static int prefixXor(int x) {
        // Pattern: 0,1,x+1,0 repeating every 4 numbers
        switch (x & 3) {
            case 0: return x;
            case 1: return 1;
            case 2: return x + 1;
            case 3: return 0;
        }
        return 0;
    }
};

int main() {
    // Example 1: Product Queries
    vector<vector<int>> queries = {{0, 0}, {1, 1}, {0, 1}};
    auto results = Solution::productQueries(13, queries);
    cout << "Product Queries Results:\n";
    for (auto r : results) cout << r << " ";
    cout << "\n\n";

    // Example 2: Modular exponentiation
    cout << "modPow(2, 10) % MOD = " << Solution::modPow(2, 10) << "\n";
    cout << "pow2mod(45) % MOD = " << Solution::pow2mod(45) << "\n\n";

    // Example 3: Count set bits
    cout << "Count of set bits in 29 = " << Solution::countSetBits(29) << "\n";
    cout << "Count of set bits in 1023 = " << Solution::countSetBits(1023) << "\n\n";

    // Example 4: Binary string representation
    cout << "Binary of 29 = " << Solution::toBinaryString(29) << "\n";
    cout << "Binary of 1023 = " << Solution::toBinaryString(1023) << "\n\n";

    // Example 5: Range XOR
    cout << "XOR of range [3, 9] = " << Solution::rangeXor(3, 9) << "\n";
    cout << "XOR of range [0, 5] = " << Solution::rangeXor(0, 5) << "\n\n";

    // Example 6: GCD and LCM
    cout << "GCD of 54 and 24 = " << Solution::gcd(54, 24) << "\n";
    cout << "LCM of 54 and 24 = " << Solution::lcm(54, 24) << "\n\n";

    // Example 7: Factorial mod
    cout << "Factorial of 10 % MOD = " << Solution::factorialMod(10) << "\n\n";

    // Example 8: Prime check
    cout << "Is 29 prime? " << (Solution::isPrime(29) ? "Yes" : "No") << "\n";
    cout << "Is 100 prime? " << (Solution::isPrime(100) ? "Yes" : "No") << "\n\n";

    // Example 9: Fibonacci mod
    cout << "Fibonacci(10) % MOD = " << Solution::fibonacciMod(10) << "\n";
    cout << "Fibonacci(50) % MOD = " << Solution::fibonacciMod(50) << "\n\n";

    // Example 10: Prefix sum
    vector<int> arr = {1, 2, 3, 4, 5};
    auto pref = Solution::prefixSum(arr);
    cout << "Prefix sums of {1,2,3,4,5}:\n";
    for (auto v : pref) cout << v << " ";
    cout << "\n";

    return 0;
}
