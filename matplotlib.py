// ---------- Continuation: More utilities (add to class Solution) ----------
public:

    // ---------- Safe Modular Helpers ----------
    static inline int modAdd(int a, int b) {
        int s = a + b;
        if (s >= MOD) s -= MOD;
        return s;
    }
    static inline int modSub(int a, int b) {
        int s = a - b;
        if (s < 0) s += MOD;
        return s;
    }
    static inline int modMul(long long a, long long b) {
        return (int)( (a*b) % MOD );
    }

    // Extended GCD -> returns gcd and sets x,y such that ax+by=g
    static long long extGcd(long long a, long long b, long long &x, long long &y) {
        if (b == 0) { x = 1; y = 0; return a; }
        long long x1, y1;
        long long g = extGcd(b, a % b, x1, y1);
        x = y1;
        y = x1 - (a / b) * y1;
        return g;
    }

    // Modular inverse using extended gcd (works even if MOD is not prime when inverse exists)
    static long long modInverseExt(long long a, long long mod) {
        long long x, y;
        long long g = extGcd(a, mod, x, y);
        if (g != 1) return -1; // inverse doesn't exist
        x %= mod;
        if (x < 0) x += mod;
        return x;
    }

    // ---------- Disjoint Set Union (Union-Find) ----------
    struct DSU {
        int n;
        vector<int> parent, sz;
        DSU(int n=0): n(n), parent(n+1), sz(n+1,1) {
            iota(parent.begin(), parent.end(), 0);
        }
        void reset(int m) {
            n = m;
            parent.resize(n+1);
            sz.assign(n+1,1);
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            return parent[x]==x ? x : parent[x]=find(parent[x]);
        }
        bool unite(int a, int b) {
            a = find(a); b = find(b);
            if (a==b) return false;
            if (sz[a] < sz[b]) swap(a,b);
            parent[b] = a;
            sz[a] += sz[b];
            return true;
        }
    };

    // ---------- Fenwick / BIT ----------
    struct Fenwick {
        int n;
        vector<long long> bit;
        Fenwick(int n=0) { init(n); }
        void init(int n_) { n = n_; bit.assign(n+1, 0); }
        void add(int idx, long long val) { for (; idx<=n; idx += idx & -idx) bit[idx] += val; }
        long long sum(int idx) { long long r=0; for (; idx>0; idx -= idx & -idx) r += bit[idx]; return r; }
        long long rangeSum(int l, int r) { return sum(r) - sum(l-1); }
    };

    // ---------- Segment Tree (sum) ----------
    struct SegmentTree {
        int n;
        vector<long long> st;
        SegmentTree() : n(0) {}
        SegmentTree(const vector<long long>& arr) { build(arr); }
        void build(const vector<long long>& arr) {
            n = arr.size();
            st.assign(4*n+4, 0);
            buildRec(1,0,n-1,arr);
        }
        void buildRec(int p,int l,int r,const vector<long long>& a) {
            if (l==r) { st[p]=a[l]; return; }
            int m=(l+r)/2;
            buildRec(p<<1,l,m,a);
            buildRec(p<<1|1,m+1,r,a);
            st[p]=st[p<<1]+st[p<<1|1];
        }
        long long query(int L,int R){ return queryRec(1,0,n-1,L,R); }
        long long queryRec(int p,int l,int r,int L,int R){
            if (L>r || R<l) return 0;
            if (L<=l && r<=R) return st[p];
            int m=(l+r)/2;
            return queryRec(p<<1,l,m,L,R) + queryRec(p<<1|1,m+1,r,L,R);
        }
        void update(int idx,long long val){ updateRec(1,0,n-1,idx,val); }
        void updateRec(int p,int l,int r,int idx,long long val){
            if (l==r){ st[p]=val; return; }
            int m=(l+r)/2;
            if (idx<=m) updateRec(p<<1,l,m,idx,val);
            else updateRec(p<<1|1,m+1,r,idx,val);
            st[p]=st[p<<1]+st[p<<1|1];
        }
    };

    // ---------- Graph Algorithms ----------
    // Dijkstra (returns distances vector)
    static vector<long long> dijkstra(int n, const vector<vector<pair<int,int>>>& adj, int src) {
        const long long INF = (1LL<<60);
        vector<long long> dist(n+1, INF);
        dist[src] = 0;
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        pq.push({0, src});
        while (!pq.empty()) {
            auto [d,u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto &e : adj[u]) {
                int v = e.first; long long w = e.second;
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        return dist;
    }

    // BFS (unweighted shortest dist)
    static vector<int> bfs(int n, const vector<vector<int>>& adj, int src) {
        const int INF = 1e9;
        vector<int> dist(n+1, INF);
        queue<int> q;
        dist[src] = 0; q.push(src);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (dist[v] == INF) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return dist;
    }

    // Topological sort (Kahn). Returns empty vector if cycle found.
    static vector<int> topoSort(int n, const vector<vector<int>>& adj) {
        vector<int> indeg(n+1,0);
        for (int u=1; u<=n; ++u)
            for (int v: adj[u]) indeg[v]++;
        queue<int> q;
        for (int i=1;i<=n;++i) if (indeg[i]==0) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int u=q.front(); q.pop();
            order.push_back(u);
            for (int v: adj[u]) {
                if (--indeg[v]==0) q.push(v);
            }
        }
        if ((int)order.size() != n) return {}; // cycle
        return order;
    }

    // Kruskal MST: input edges as (w,u,v), returns mst weight and edges used
    static pair<long long, vector<tuple<int,int,int>>> kruskal(int n, vector<tuple<int,int,int>> edges) {
        sort(edges.begin(), edges.end()); // sort by weight
        DSU dsu(n);
        long long total = 0;
        vector<tuple<int,int,int>> used;
        for (auto &e : edges) {
            int w,u,v; tie(w,u,v) = e;
            if (dsu.unite(u,v)) {
                total += w;
                used.push_back(e);
            }
        }
        return {total, used};
    }

    // Count connected components (undirected)
    static int countComponents(int n, const vector<vector<int>>& adj) {
        vector<char> vis(n+1, 0);
        int cnt = 0;
        for (int i=1;i<=n;++i) {
            if (!vis[i]) {
                cnt++;
                stack<int> st; st.push(i); vis[i]=1;
                while (!st.empty()) {
                    int u = st.top(); st.pop();
                    for (int v: adj[u]) if (!vis[v]) { vis[v]=1; st.push(v); }
                }
            }
        }
        return cnt;
    }

    // ---------- Strings: KMP / Z-function / Rolling Hash ----------
    static vector<int> computeLPS(const string &pat) {
        int n = pat.size();
        vector<int> lps(n, 0);
        for (int i=1, len=0; i<n; ) {
            if (pat[i]==pat[len]) lps[i++] = ++len;
            else if (len) len = lps[len-1];
            else lps[i++] = 0;
        }
        return lps;
    }
    // KMP search: returns starting indices of matches
    static vector<int> kmpSearch(const string &text, const string &pat) {
        if (pat.empty()) return {};
        vector<int> res;
        auto lps = computeLPS(pat);
        int i=0, j=0, n=text.size(), m=pat.size();
        while (i<n) {
            if (text[i]==pat[j]) { i++; j++; if (j==m) { res.push_back(i-j); j=lps[j-1]; } }
            else if (j) j = lps[j-1];
            else i++;
        }
        return res;
    }

    static vector<int> zFunction(const string &s) {
        int n = s.size();
        vector<int> z(n, 0);
        int l=0, r=0;
        for (int i=1; i<n; ++i) {
            if (i<=r) z[i] = min(r-i+1, z[i-l]);
            while (i+z[i] < n && s[z[i]] == s[i+z[i]]) z[i]++;
            if (i+z[i]-1 > r) l=i, r=i+z[i]-1;
        }
        z[0] = n;
        return z;
    }

    // Rolling Hash (Rabin-Karp) - 64-bit to avoid mod
    struct RollingHash {
        long long base;
        vector<unsigned long long> pref, power;
        RollingHash(const string &s, long long base = 91138233LL) : base(base) {
            int n = s.size();
            pref.assign(n+1,0);
            power.assign(n+1,1);
            for (int i=0;i<n;++i) {
                pref[i+1] = pref[i]*base + (unsigned char)s[i] + 1;
                power[i+1] = power[i]*base;
            }
        }
        unsigned long long get(int l,int r){ // [l,r)
            return pref[r] - pref[l]*power[r-l];
        }
    };

    // ---------- Number Theory: smallest prime factor sieve & factorization ----------
    static vector<int> spfSieve(int n) {
        vector<int> spf(n+1);
        for (int i=2;i<=n;++i) spf[i]=0;
        for (int i=2;i<=n;++i) {
            if (spf[i]==0) {
                spf[i]=i;
                if ((long long)i*i <= n) {
                    for (int j=i*i;j<=n;j+=i) if (spf[j]==0) spf[j]=i;
                }
            }
        }
        return spf;
    }
    static vector<pair<int,int>> factorizeWithSPF(int x, const vector<int>& spf) {
        vector<pair<int,int>> res;
        while (x>1) {
            int p = spf[x];
            int cnt = 0;
            while (x%p==0) { x/=p; ++cnt; }
            res.push_back({p,cnt});
        }
        return res;
    }

    // Simple prime factorization for single number (works up to sqrt(n))
    static vector<pair<long long,int>> primeFactorize(long long n) {
        vector<pair<long long,int>> res;
        for (long long p=2; p*p<=n; ++p) {
            if (n%p==0) {
                int c=0;
                while (n%p==0) { n/=p; ++c; }
                res.push_back({p,c});
            }
        }
        if (n>1) res.push_back({n,1});
        return res;
    }

    // ---------- Binary search helpers ----------
    // lower_bound on vector
    template<typename T>
    static int lowerBoundIdx(const vector<T>& a, const T& key) {
        return int(lower_bound(a.begin(), a.end(), key) - a.begin());
    }
    template<typename T>
    static int upperBoundIdx(const vector<T>& a, const T& key) {
        return int(upper_bound(a.begin(), a.end(), key) - a.begin());
    }

    // ---------- Bitmask DP helper (iterate submasks) ----------
    // iterate all submasks of mask: for (int s = mask; s; s = (s-1)&mask) { ... } and include 0 if needed

    // ---------- Utilities ----------
    // clamp value
    template<typename T>
    static T clampVal(T x, T lo, T hi) { return x < lo ? lo : (x > hi ? hi : x); }

    // join vector to string with separator (for debug/printing)
    template<typename T>
    static string join(const vector<T>& a, const string& sep=", ") {
        ostringstream oss;
        for (size_t i=0;i<a.size();++i) {
            if (i) oss << sep;
            oss << a[i];
        }
        return oss.str();
    }

    // ---------- Misc Helpers ----------
    // Convert integer to vector of digits (base 10)
    static vector<int> digits(int x) {
        if (x==0) return {0};
        vector<int> d;
        while (x>0) { d.push_back(x%10); x/=10; }
        reverse(d.begin(), d.end());
        return d;
    }

    // Next permutation (wrapper)
    template<typename T>
    static bool nextPerm(vector<T>& a) { return next_permutation(a.begin(), a.end()); }

    // Prev permutation (wrapper)
    template<typename T>
    static bool prevPerm(vector<T>& a) { return prev_permutation(a.begin(), a.end()); }

    // Count set bits in 64-bit
    static int countSetBits64(long long x) { return __builtin_popcountll((unsigned long long)x); }

    // Fast power for long long (non-modular)
    static long long powll(long long a, long long e) {
        long long r = 1;
        while (e>0) {
            if (e&1) r = r*a;
            a = a*a;
            e >>= 1;
        }
        return r;
    }

    // Ceiling of integer division
    static long long ceilDiv(long long a, long long b) {
        if (b<0) a=-a, b=-b;
        if (b==0) throw runtime_error("division by zero");
        return (a + b - 1) / b;
    }

}; // end class Solution

// ---------------------------- Example usage notes ----------------------------
// - Many of these helpers are static and can be called as Solution::dijkstra(...), etc.
// - DSU, Fenwick, SegmentTree are nested types and can be instantiated with Solution::DSU d(n);
// - KMP usage: auto occ = Solution::kmpSearch(text, pattern);
// - RollingHash: RollingHash rh(s); auto h = rh.get(l, r); // [l,r)
// -----------------------------------------------------------------------------
