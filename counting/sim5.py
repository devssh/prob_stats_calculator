def hats1():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4], size=1000000,
                                  p=[1 / 4, 1 / 4, 1 / 4, 1 / 4])
    size = 4
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        if len(list(set(committee))) < 4:
            continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        # if len([i for i in arr if i == 3]) >= 1:
        if arr[0] == 1 and (arr[1] == 2) and (arr[2] == 3) and (arr[3] == 4):
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(1 / factorial(4))


def hats2():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4], size=1000000,
                                  p=[1 / 4, 1 / 4, 1 / 4, 1 / 4])
    size = 4
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        if len(list(set(committee))) < 4:
            continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        # if len([i for i in arr if i == 3]) >= 1:
        if arr[0] == 1 and (arr[1] == 2) and (arr[2] == 3):
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(factorial(4 - 3) / factorial(4))


def hats23():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4, 5], size=1000000,
                                  p=[1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5])
    size = 5
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        if len(list(set(committee))) < size:
            continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        # if len([i for i in arr if i == 3]) >= 1:
        if arr[0] == 1 and (arr[1] == 2) and (arr[2] == 3):
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(factorial(5 - 3) / factorial(5))


# hats23()

def hats3():
    import numpy as np

    total_size = 5
    coin_flips = np.random.choice(list(range(1, total_size + 1)), size=1000000,
                                  p=[1 / total_size for _ in list(range(1, total_size + 1))])
    size = 5
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        if len(list(set(committee))) < size:
            continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        # if len([i for i in arr if i == 3]) >= 1:
        if arr[0] == 2 and (arr[1] == 3) and (arr[2] == 4):
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(1 / comb(5, 3))
    print(3 / comb(5, 3))
    print((5 - 3) / comb(5, 3))
    print(5 / comb(5, 3))


# hats3() # wtf? they exchanged combination and permutation notation


def hats4():
    import numpy as np

    total_size = 5
    coin_flips = np.random.choice(list(range(1, total_size + 1)), size=10000000,
                                  p=[1 / total_size for _ in list(range(1, total_size + 1))])
    size = 5
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        if len(list(set(committee))) < size:
            continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        # if len([i for i in arr if i == 3]) >= 1:
        dirty = np.random.choice([0, 1], size=total_size, p=[0.25, 0.75])
        if dirty[0] == 1 and (dirty[1] == 1) and (dirty[2] == 1):
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(pow(0.75, 3))


def hats5():
    import numpy as np

    total_size = 5
    coin_flips = np.random.choice(list(range(1, total_size + 1)), size=10000000,
                                  p=[1 / total_size for _ in list(range(1, total_size + 1))])
    size = 5
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        if len(list(set(committee))) < size:
            continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        # if len([i for i in arr if i == 3]) >= 1:
        dirty = np.random.choice([0, 1], size=total_size, p=[0.25, 0.75])
        if len([i for i in dirty if i == 1]) == 3:
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(comb(5, 3) * pow(0.75, 3) * pow(0.25, 2))
