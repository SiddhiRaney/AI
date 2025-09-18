
public:

    // ---------------------- Modular exponentiation (modular pow) ----------------------
    // computes a^e % mod (mod fits in 64-bit)
    static long long modPow(long long a, long long e, long long mod) {
        a %= mod;
        long long res = 1 % mod;
        while (e > 0) {
            if (e & 1) res = (__int128)res * a % mod;
            a = (__int128)a * a % mod;
            e >>= 1;
        }
        return res;
    }

    // ---------------------- Precompute factorials / inverse factorials ----------------------
    // call initFactorials(maxN, MOD) to precompute for nCr modulo MOD
    static vector<long long> fact, invfact;
    static void initFactorials(int maxN, int mod) {
        fact.assign(maxN+1, 1);
        invfact.assign(maxN+1, 1);
        for (int i=1;i<=maxN;++i) fact[i] = fact[i-1] * i % mod;
        invfact[maxN] = modInverseExt(fact[maxN], mod);
        for (int i=maxN;i>0;--i) invfact[i-1] = invfact[i] * i % mod;
    }
    static long long nCrMod(long long n, long long r, int mod) {
        if (r<0 || r>n) return 0;
        return fact[n] * invfact[r] % mod * invfact[n-r] % mod;
    }

    // ---------------------- Simple sieve of primes ----------------------
    static vector<int> sievePrimes(int n) {
        vector<char> isPrime(n+1, true);
        vector<int> primes;
        if (n < 2) return primes;
        isPrime[0]=isPrime[1]=false;
        for (int i=2;i<=n;++i) {
            if (isPrime[i]) {
                primes.push_back(i);
                if ((long long)i * i <= n)
                    for (int j=i*i; j<=n; j+=i) isPrime[j]=false;
            }
        }
        return primes;
    }

    // ---------------------- Miller-Rabin primality test (deterministic for 64-bit) ----------------------
    static bool millerRabinDet(long long n) {
        if (n<2) return false;
        for (long long p : {2,3,5,7,11,13,17,19,23,29,31,37}) {
            if (n%p==0) return n==p;
        }
        long long d = n-1, s = 0;
        while ((d & 1) == 0) { d >>= 1; ++s; }
        // bases for deterministic 64-bit test
        long long bases[] = {2,325,9375,28178,450775,9780504,1795265022};
        for (long long a : bases) {
            if (a % n == 0) continue;
            long long x = modPow(a, d, n);
            if (x==1 || x==n-1) continue;
            bool composite = true;
            for (int r=1;r<s;++r) {
                x = (__int128)x * x % n;
                if (x == n-1) { composite = false; break; }
            }
            if (composite) return false;
        }
        return true;
    }

    // ---------------------- Baby-step Giant-step (discrete log) ----------------------
    // solves a^x = b (mod m), returns x >= 0 or -1 if no solution (m doesn't have to be prime)
    static long long babyStepGiantStep(long long a, long long b, long long m) {
        a %= m; b %= m;
        if (m==1) return 0;
        long long cnt = 0;
        long long t = 1;
        long long g;
        while ((g = std::gcd(a, m)) > 1) {
            if (b == t) return cnt;
            if (b % g) return -1;
            b /= g; m /= g; t = t * (a/g) % m;
            ++cnt;
        }
        long long n = (long long) sqrt(m) + 1;
        unordered_map<long long,long long> vals;
        long long an = 1;
        for (long long i=0;i<n;++i) an = (__int128)an * a % m;
        long long cur = b;
        for (long long q=0;q<=n;++q) {
            vals[cur] = q;
            cur = (__int128)cur * a % m;
        }
        cur = t;
        for (long long p=1;p<=n+1;++p) {
            if (vals.count(cur)) {
                long long ans = p*n - vals[cur] + cnt;
                return ans;
            }
            cur = (__int128)cur * an % m;
        }
        return -1;
    }

    // ---------------------- Chinese remainder theorem ----------------------
    // given pairs (r_i, m_i) with pairwise-coprime m_i, returns x mod M (or { -1, -1 } if no solution)
    static pair<long long,long long> crt(const vector<long long>& r, const vector<long long>& m) {
        long long x = 0;
        long long M = 1;
        int k = r.size();
        for (int i=0;i<k;++i) M *= m[i];
        for (int i=0;i<k;++i) {
            long long Mi = M / m[i];
            long long inv = modInverseExt(Mi % m[i], m[i]);
            if (inv == -1) return {-1,-1};
            x = (x + (__int128)r[i] * Mi % M * inv) % M;
        }
        if (x < 0) x += M;
        return {x, M};
    }

    // ---------------------- 0-1 BFS (shortest path for 0/1 weighted edges) ----------------------
    static vector<long long> zeroOneBFS(int n, const vector<vector<pair<int,int>>>& adj, int src) {
        const long long INF = (1LL<<60);
        deque<int> dq;
        vector<long long> dist(n+1, INF);
        dist[src] = 0;
        dq.push_back(src);
        while (!dq.empty()) {
            int u = dq.front(); dq.pop_front();
            for (auto &e : adj[u]) {
                int v = e.first; int w = e.second;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    if (w == 0) dq.push_front(v);
                    else dq.push_back(v);
                }
            }
        }
        return dist;
    }

    // ---------------------- Kosaraju SCC (strongly connected components) ----------------------
    static vector<int> kosarajuSCC(int n, const vector<vector<int>>& adj) {
        vector<char> vis(n+1, 0);
        vector<int> order;
        function<void(int)> dfs1 = [&](int u) {
            vis[u]=1;
            for (int v: adj[u]) if (!vis[v]) dfs1(v);
            order.push_back(u);
        };
        for (int i=1;i<=n;++i) if (!vis[i]) dfs1(i);
        vector<vector<int>> radj(n+1);
        for (int u=1;u<=n;++u) for (int v: adj[u]) radj[v].push_back(u);
        vector<int> comp(n+1, 0);
        int cid = 0;
        function<void(int)> dfs2 = [&](int u) {
            comp[u] = cid;
            for (int v: radj[u]) if (!comp[v]) dfs2(v);
        };
        for (int i = (int)order.size()-1; i>=0; --i) {
            int u = order[i];
            if (!comp[u]) { ++cid; dfs2(u); }
        }
        // comp[1..n] gives component id (1..cid)
        return comp;
    }

    // ---------------------- Binary lifting LCA (1-indexed nodes) ----------------------
    struct LCA {
        int n, LOG;
        vector<vector<int>> up;
        vector<int> depth;
        LCA() : n(0), LOG(0) {}
        void build(const vector<vector<int>>& tree, int root = 1) {
            n = tree.size()-1;
            LOG = 1;
            while ((1<<LOG) <= n) ++LOG;
            up.assign(LOG, vector<int>(n+1, 0));
            depth.assign(n+1, 0);
            function<void(int,int)> dfs = [&](int u, int p) {
                up[0][u] = p;
                for (int k=1;k<LOG;++k) up[k][u] = up[k-1][u] ? up[k-1][ up[k-1][u] ] : 0;
                for (int v: tree[u]) if (v!=p) {
                    depth[v] = depth[u] + 1;
                    dfs(v, u);
                }
            };
            depth[root] = 0;
            dfs(root, 0);
        }
        int lift(int u, int k) {
            for (int i=0;i<LOG && u; ++i) if (k & (1<<i)) u = up[i][u];
            return u;
        }
        int lca(int a, int b) {
            if (depth[a] < depth[b]) swap(a,b);
            a = lift(a, depth[a]-depth[b]);
            if (a==b) return a;
            for (int k=LOG-1;k>=0;--k) if (up[k][a] != up[k][b]) {
                a = up[k][a]; b = up[k][b];
            }
            return up[0][a];
        }
    };

    // ---------------------- Dinic max-flow ----------------------
    struct Dinic {
        struct Edge { int v; long long cap; int rev; };
        int N;
        vector<vector<Edge>> G;
        vector<int> level, it;
        Dinic(int n=0) { init(n); }
        void init(int n) { N=n; G.assign(N, {}); level.assign(N,0); it.assign(N,0); }
        void addEdge(int u,int v,long long c) {
            Edge a = {v, c, (int)G[v].size()};
            Edge b = {u, 0, (int)G[u].size()};
            G[u].push_back(a);
            G[v].push_back(b);
        }
        bool bfs(int s,int t) {
            fill(level.begin(), level.end(), -1);
            queue<int> q; q.push(s); level[s]=0;
            while (!q.empty()) {
                int u=q.front(); q.pop();
                for (auto &e: G[u]) if (e.cap>0 && level[e.v]==-1) {
                    level[e.v]=level[u]+1; q.push(e.v);
                }
            }
            return level[t] != -1;
        }
        long long dfs(int u,int t,long long f) {
            if (u==t) return f;
            for (int &i = it[u]; i<(int)G[u].size(); ++i) {
                Edge &e = G[u][i];
                if (e.cap > 0 && level[e.v] == level[u] + 1) {
                    long long got = dfs(e.v, t, min(f, e.cap));
                    if (got > 0) {
                        e.cap -= got;
                        G[e.v][e.rev].cap += got;
                        return got;
                    }
                }
            }
            return 0;
        }
        long long maxFlow(int s,int t) {
            long long flow = 0;
            while (bfs(s,t)) {
                fill(it.begin(), it.end(), 0);
                while (true) {
                    long long pushed = dfs(s,t, (1LL<<60));
                    if (!pushed) break;
                    flow += pushed;
                }
            }
            return flow;
        }
    };

    // ---------------------- Useful small helpers ----------------------
    static bool isPowerOfTwo(long long x) { return x > 0 && (x & (x-1)) == 0; }
    static long long nextPowerOfTwo(long long x) {
        if (x <= 1) return 1;
        --x;
        for (int i=1;i<63;i<<=1) x |= x >> i;
        return x+1;
    }

    // ---------------------- Notes ----------------------
    // - Add `Solution::fact` and `Solution::invfact` declarations in a .cpp file if using multiple translation units:
    //     vector<long long> Solution::fact; vector<long long> Solution::invfact;
    // - Use these helpers as: Solution::modPow(a,e,mod), Solution::initFactorials(maxN, MOD), Solution::nCrMod(n,r,MOD), etc.
    // - Dinic expects 0-indexed nodes for simplicity inside its struct; adapt when calling if your graph is 1-indexed.
    // -----------------------------------------------------------------------------

