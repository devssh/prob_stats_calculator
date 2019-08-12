from counting.sim2 import comb

print(5 * comb(10, 5))
print(10 * comb(9, 4))

print(comb(10, 5), 2 * comb(9, 4))  # only works if 2n C n
print(comb(12, 6), 2 * comb(11, 5))
