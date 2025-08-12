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
    cout << "XOR of range [0, 5] = " << Solution::rangeXor(0, 5) << "\n";

    return 0;
}
