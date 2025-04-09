from timeit import timeit

import sys
sys.set_int_max_str_digits(1000000) 

bigonacci_result = {}

def recursive_simple(n):
    if n == 0 or n == 1:
        bigonacci_result["recursive_simple"] = {"n" : n, "f(n)" : n}
        return bigonacci_result["recursive_simple"]["f(n)"]
    else:
        bigonacci_result["recursive_simple"] = {"n" : n, "f(n)" : recursive_simple(n - 1) + recursive_simple(n - 2)}
        return bigonacci_result["recursive_simple"]["f(n)"]
    
def iterative_simple(n):
    if n == 0 or n == 1:
        return n
    else:
        n_0, n_1 = 0, 1
        for n_2 in range(2, n + 1):
            n_2 = n_1 + n_0
            n_0, n_1 = n_1, n_2
        bigonacci_result["iterative_simple"] = {"n" : n, "f(n)" : n_2}
        return bigonacci_result["iterative_simple"]["f(n)"]

memo = {0 : 0, 1 : 1}
def recursive_memoised(n):
    if n in memo:
        bigonacci_result["recursive_memoised"] = {"n" : n, "f(n)" : memo[n]}
        return bigonacci_result["recursive_memoised"]["f(n)"]
    else:
        bigonacci_result["recursive_memoised"] = {"n" : n, "f(n)" : recursive_memoised(n - 1) + recursive_memoised(n - 2)}
        memo[n] = bigonacci_result["recursive_memoised"]["f(n)"]
        return bigonacci_result["recursive_memoised"]["f(n)"]
    
approaches = [recursive_memoised]
max_n = 996

for fn in approaches:
    for n in range(0, max_n, 1):
        t = timeit(f"fn({n})", number=1, globals=globals())
        memo = {0 : 0, 1 : 1}
        print(n, t)
        if t >= 1:
            break

import json

with open("output.json", "w") as output_file:
    json.dump(bigonacci_result, output_file) 