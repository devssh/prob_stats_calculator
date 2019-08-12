def committee():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=100000,
                                  p=[1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10,
                                     1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10])
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
        if len([i for i in arr if i <= 5]) == 2 and (len([i for i in arr if i > 5]) == 2):
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb

    print((comb(5, 2) * comb(5, 2)) / comb(10, 4))


def committee2():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=100000,
                                  p=[1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10,
                                     1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10])
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
        men_count = len([i for i in arr if i <= 5])
        if len([i for i in arr if i > 5]) > men_count:
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb

    print((comb(5, 3) * comb(5, 1) + comb(5, 4)) / comb(10, 4))


def committee3():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=100000,
                                  p=[1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10,
                                     1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10])
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
        men_count = len([i for i in arr if i <= 5])
        if men_count >= 1:
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb

    print(1 - ((comb(5, 4)) / comb(10, 4)))


import numpy as np

coin_flips = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=100000,
                              p=[1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10,
                                 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10])
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
    if len([i for i in arr if i == 1]) > 0 and (len([i for i in arr if i == 6]) > 0):
        num_count = num_count + 1
    denom_count = denom_count + 1
prob = num_count / denom_count
print(prob)
print(denom_count)

from counting.sim2 import comb

print((comb(4, 2)*21 + comb(4, 1) * comb(4, 1)) / comb(10, 4))
