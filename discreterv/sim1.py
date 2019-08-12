def die1():
    import numpy as np

    coin_flips = np.random.choice([1, 2, 3, 4, 5, 6], size=100000,
                                  p=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    size = 5
    coin_flips1 = [int(i) for i in coin_flips]
    coin_flips = []
    for i in range(int(len(coin_flips1) / size)):
        print(i)
        committee = coin_flips1[i * size:i * size + size]
        # if len(list(set(committee))) < size:
        #     continue
        coin_flips = [*coin_flips, committee]

    num_count = 0
    denom_count = 0
    for arr in coin_flips:
        if len([i for i in arr if i == 3 or i == 2]) == 1:
            num_count = num_count + 1
        denom_count = denom_count + 1
    prob = num_count / denom_count
    print(prob)
    print(denom_count)

    from counting.sim2 import comb, factorial

    print(1 / factorial(4))


# die1()


def hats23():
    import numpy as np
    import itertools
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = list(itertools.permutations(mylist))
    denom = len(total)
    print(denom)
    num = len([x for x in total if (x[2] == 3) and (x[5] == 6) and (x[6] == 7)])
    print(num)
    print(num/denom)

hats23()
