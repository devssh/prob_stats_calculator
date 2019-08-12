# import numpy as np
#
# sum = 0
# trials = 100000
# for i in range(trials):
#     print(i)
#     burn = np.random.choice([0, 1], p=[1 / 3, 2 / 3])
#     if burn == 1:
#         choice = np.random.choice(np.linspace(0, 3, 300), p=[1 / 300] * 300)
#         sum = sum + choice
#
# print(sum/trials)


# import numpy as np
#
# num = 0
# trials = 100000
# for i in range(trials):
#     print(i)
#     x = np.random.choice(np.linspace(0, 40, 400), p=[1 / 400] * 400)
#     y = np.random.choice(np.linspace(0, 3 * x, 1200), p=[1 / 1200] * 1200)
#     if (y - x) > 0:
#         num = num + 1
#
# print(num / trials)

import numpy as np

l = list(np.linspace(0, 1 / 200, 400))
print(sum(l), len(l))

num = 0
trials = 10000000
for i in range(trials):
    print(i, num/(i+1))
    x = np.random.choice(np.linspace(0, 40, 400), p=np.linspace(0, 1/200, 400)) # why  is it not 0 to 1/20
    y = np.random.choice(np.linspace(0, 3 * x, 1200), p=[1 / 1200] * 1200)
    num = num + (y - x)

print(num)
print(num/trials)
