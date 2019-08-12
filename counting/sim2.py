def die():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3], size=1000002, p=[1 / 2, 1 / 4, 1 / 4])
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / 6)):
        print(i)
        coin_flips = [*coin_flips, coin_flips1[i * 6:i * 6 + 6]]

    num_count = 0
    for arr in coin_flips:
        if len([i for i in arr if i == 3]) == 2:
            num_count = num_count + 1
    prob = num_count / (len(coin_flips1) / 6)
    print(prob)


def die_conditional():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3], size=1000002, p=[1 / 2, 1 / 4, 1 / 4])
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / 6)):
        print(i)
        coin_flips = [*coin_flips, coin_flips1[i * 6:i * 6 + 6]]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        if len([i for i in arr if i == 1]) == 2:
            if arr[0] == 1:
                num_count = num_count + 1
            denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)


def die_conditional2():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3], size=1000002, p=[1 / 2, 1 / 4, 1 / 4])
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / 6)):
        print(i)
        coin_flips = [*coin_flips, coin_flips1[i * 6:i * 6 + 6]]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        if len([i for i in arr if i == 1]) == 3 and (len([i for i in arr if i == 2]) == 3):
            if (arr[0] == 1) and (arr[1] == 2) and (arr[2] == 1) and (arr[3] == 2) and (arr[4] == 1) and (arr[5] == 2):
                num_count = num_count + 1
            denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def comb(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def find_natural():
    fak = 2
    RHS = 0.36
    # RHS = 0.42
    upto = 7
    for i in range(upto):
        for j in range(1, upto):
            for k in range(2, upto):
                if pow(i / j, k) == 1:
                    continue
                LHS = (1 / (1 - pow(i / j, k))) * comb(k, fak) * pow(1 / j, fak) * pow(i / j, k - fak)
                if abs(LHS - RHS) < 0.01:
                    print(i, j, k)


# find_natural()
# fak = 3
# i = 3
# j = 4
# k = 6
# LHS = (1 / (1 - pow(i / j, k))) * comb(k, fak) * pow(1 / j, fak) * pow(i / j, k - fak)
# print(LHS)


def die_cond3():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3], size=100002, p=[1 / 2, 1 / 4, 1 / 4])
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / 6)):
        print(i)
        coin_flips = [*coin_flips, coin_flips1[i * 6:i * 6 + 6]]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        if len([i for i in arr if i == 3]) >= 1:
            if len([i for i in arr if i == 3]) == 3:
                num_count = num_count + 1
            denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)
