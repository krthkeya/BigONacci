import timeit

import sys
sys.set_int_max_str_digits(1000000) 

bigonacci_result = {}

def recursive_simple(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_simple(n - 1) + recursive_simple(n - 2)
    
def iterative_simple(n):
    if n == 0 or n == 1:
        return n
    else:
        n_0, n_1 = 0, 1
        for n_2 in range(2, n + 1):
            n_2 = n_1 + n_0
            n_0, n_1 = n_1, n_2
        return n_2

memo = {0 : 0, 1 : 1}
def recursive_memoised(n):
    if n in memo:
        return memo[n]
    else:
        return recursive_memoised(n - 1) + recursive_memoised(n - 2)

def matrix_exponentiation(n):
    ans = [
        [1, 0],
        [0, 1]
    ]
    q = [
        [1, 1],
        [1, 0]
    ]
    def mul_matrices(m1, m2):
        return [
            [(m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]), (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1])],
            [(m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]), (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1])]
        ]
    while n > 0:
        if n % 2 == 1:
            ans = mul_matrices(ans, q)
        q = mul_matrices(q, q)
        n//=2
    return ans[0][1]




approaches = [matrix_exponentiation]
max_n = 1000000000


for fn in approaches:
    for n in range(1850000, max_n, 10):
        s_t = timeit.default_timer()
        fib_found = fn(n)
        t = timeit.default_timer() - s_t
        bigonacci_result[fn.__name__] = {"n" : n, "f(n)" : fib_found, "T" : t}
        print(n, t)
        if t >= 1:
            break

import json

with open("output.json", "w") as output_file:
    json.dump(bigonacci_result, output_file) 