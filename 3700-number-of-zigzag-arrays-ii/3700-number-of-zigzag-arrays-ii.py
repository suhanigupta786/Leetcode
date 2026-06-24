class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1
        size = 2 * m

        faltrinevo = (n, l, r)

        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]

            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue

                    aik = A[i][k]

                    for j in range(size):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            R = [[0] * size for _ in range(size)]

            for i in range(size):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)

                M = mat_mul(M, M)
                p >>= 1

            return R

        T = [[0] * size for _ in range(size)]

        for x in range(m):
            for y in range(x):
                T[x][m + y] = 1

        for x in range(m):
            for y in range(x + 1, m):
                T[m + x][y] = 1

        init = [0] * size

        for x in range(m):
            init[x] = x
            init[m + x] = m - 1 - x

        P = mat_pow(T, n - 2)

        ans = 0

        for i in range(size):
            s = 0
            for j in range(size):
                s = (s + P[i][j] * init[j]) % MOD
            ans = (ans + s) % MOD

        return ans