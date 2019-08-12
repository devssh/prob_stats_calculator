#
import numpy as np
#
# l = list(np.linspace(0, 1 / 200, 400))
# print(sum(l), len(l))
#
# num = 0
# trials = 100000
# for i in range(trials):
#     print(i, num/(i+1))
#     x = np.random.choice(np.linspace(0, 40, 400), p=np.linspace(0, 1/200, 400)) # why  is it not 0 to 1/20
#     y = np.random.choice(np.linspace(0, 3 * x, 1200), p=[1 / 1200] * 1200)
#     num = num + (y - x)
#
# print(num)
# print(num/trials)

sum = 0
var = 0

for i in range(2, 10000):
    sum = sum + ((5 * i)/2)
    var = var
    print(sum)
x = pow(5, 2)/12
y = pow(5, 4)/pow(12, 3)
print(x, y, x+y)