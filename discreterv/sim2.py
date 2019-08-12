# import numpy as np
#
# n = 10
# size = 5
# p = 1 / n
# num = 0
# denom = 0
# from counting.sim2 import comb, factorial
# trials = 1000000
# for i in range(trials):
#     if i % 100000 == 0:
#         print("proc", i*100/trials, "%")
#     coin_flips = np.random.choice(list(range(n)), size=size,
#                                   p=[1 / n] * n, replace=True)
#     if len(set(coin_flips)) == size:
#         num = num + 1
#     denom = denom + 1
#
# print(num / denom, num, denom)
# print(comb(n, size) * factorial(size) / pow(n, size))

# import numpy as np
#
# n = 20
# k = 4
# p = 1 / n
# num = 0
# denom = 0
# from counting.sim2 import comb, factorial
#
# trials = 1000000
# for i in range(trials):
#     if i % 10000 == 0:
#         print("proc", i * 100 / trials, "%")
#     coin_flips = np.random.choice(list(range(1, n+1)), size=k,
#                                   p=[1 / n] * n, replace=False)
#     if sorted(coin_flips)[1] == 7:
#         num = num + 1
#     denom = denom + 1

# print(num / denom, num, denom)
# print(2 * 1 * 7 * 6 / (2*comb(n, k)))
# print(6 * 1 * 13 * 12 / (2*comb(20, 4)))
# 0.096355

#
# import numpy as np
#
# n = 5
# k = 2 * n
# p = 1 / n
# num = 0
# denom = 0
# from counting.sim2 import comb, factorial
#
# trials = 100000
# for i in range(trials):
#     bins = [0] * n
#     if i % 10000 == 0:
#         print("proc", i * 100 / trials, "%")
#     coin_flips = np.random.choice(list(range(1, n + 1)), size=k,
#                                   p=[1 / n] * n, replace=True)
#     for coin in coin_flips:
#         bins[coin - 1] = bins[coin - 1] + 1
#     if bins[0] == 0:
#         num = num + 1
#     denom = denom + 1
# print(num / denom, num, denom)
# print(pow((n - 1) / n, k))

#
# import numpy as np
#
# n = 5
# k = 2 * n
# p = 1 / n
# num = 0
# denom = 0
# from counting.sim2 import comb, factorial
#
# trials = 100000
# for i in range(trials):
#     bins = [0] * n
#     if i % 10000 == 0:
#         print("proc", i * 100 / trials, "%")
#     coin_flips = np.random.choice(list(range(1, n + 1)), size=k,
#                                   p=[1 / n] * n, replace=True)
#     for coin in coin_flips:
#         bins[coin - 1] = bins[coin - 1] + 1
#     num = num + len([b for b in bins if b==0])
#     denom = denom + 1
# print(num / denom, num, denom)
# print(n * pow((n - 1) / n, k))


import numpy as np

n = 6
p = 1 / n
num = 0
denom = 0
from counting.sim2 import comb, factorial

trials = 100000
for i in range(trials):
    k = np.random.choice(list(range(4)), p=[1/4]*4)
    if i % 10000 == 0:
        print("proc", i * 100 / trials, "%")
    coin_flips = np.random.choice(list(range(1, n + 1)), size=k,
                                  p=[1 / n] * n, replace=True)
    if len([x for x in coin_flips if x in [5, 6]]) == 2:
        if k ==3:
            num = num + 1
        denom = denom + 1
print(num / denom, num, denom)
# print(n)
