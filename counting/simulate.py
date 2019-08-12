def count(output, condition_num, condition_denom):
    return len([i for i in output if condition_num(i)]) / len([i for i in output if condition_denom(i)])


max_error = 0
# for i in range(500):
import numpy as np

coin_flips = np.random.choice([1, 2, 3], size=100002, p=[1 / 3, 1 / 3, 1 / 3])
coin_flips1 = [int(i) for i in coin_flips]
coin_flips = []
for i in range(int(len(coin_flips1) / 6)):
    print(i)
    coin_flips = [*coin_flips, coin_flips1[i * 6:i * 6 + 6]]

num_count = 0
for arr in coin_flips:
    if len([i for i in arr if i == 1]) == 1:
        num_count = num_count + 1
prob = num_count / (len(coin_flips1)/6)
# if abs(prob - 0.5) > max_error:
#     max_error = abs(prob - 0.5)
print(prob)

# print(max_error)
