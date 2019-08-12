import math
# from statistics import NormalDist
from scipy.stats import norm


def phi(x0, mu=0.0, var=1.0, greater_than=False, precision=4):
    x = round(x0, 2)
    # for CDF of normal distribution with X < x
    # print("phi ", mu, var, x)
    if greater_than:
        return 1.0 - ((1.0 + math.erf((x - mu) / math.sqrt(2.0 * var))) / 2.0)
    return round((1.0 + math.erf((x - mu) / math.sqrt(2.0 * var))) / 2.0, precision)


def phi_between(x1, x2, mu=0.0, var=1.0):
    return phi(x2, mu, var) - phi(x1, mu, var)


def phi_inverse(prob, mu=0.0, var=1.0, error_less_than=False):
    if error_less_than:
        return norm.ppf(1 - prob, loc=mu, scale=math.sqrt(var))
    return norm.ppf(prob, loc=mu, scale=math.sqrt(var))


def clt_phi_get_prob(a=210.0, mu=2.0, sigma=2.0, n=100.0, greater_than=True):
    # (Sn - n*mu)/(sqrt(n)*sigma) where denom is s.d.
    # P(Sn >= a) = ?
    return phi(a, n * mu, n * pow(sigma, 2), greater_than=greater_than)


def clt_phi_get_prob_binom(a=21.0, n=36.0, p=0.5, greater_than=False):
    return clt_phi_get_prob(a, p, math.sqrt(p * (1 - p)), n, greater_than)


def clt_phi_get_inverse_param(prob=0.05, mu=2, sigma=2, n=100, confidence_greater_than=False):
    # norm.ppf is inverse of norm.cdf, scale is s.d, loc is mu
    # P(Sn >= ?) approx = 0.05
    if confidence_greater_than:
        return norm.ppf(prob, loc=mu * n, scale=sigma * math.sqrt(n))
    return norm.ppf(1 - prob, loc=mu * n, scale=sigma * math.sqrt(n))
    # return NormalDist(mu=n*mu, sigma=sigma*math.sqrt(n)).inv_cdf(prob)


def clt_phi_get_n(prob=0.05, mu=2, var=4, a=210, confidence_greater_than=False):
    # def clt_phi_get_n_helper(prob=0.05, mu=0, var=1, a=210, confidence_greater_than=False):
    # after getting phi_value try to solve phi(0.05) = 1 - phi(0.95) = P(( (Sn - mu*n)/(var*sqrt(n)) ) >=
    #  ( (a - (mu*n))/(var*sqrt(n)) ) )
    # i.e in this case phi(0.95) = 1.645 = (210 - 2*n)/(2*sqrt(n))
    # number of packages = n, weight total = 210,
    # exponential distribution with lambda = 1/2 implies CLT with mu = sigma = 2
    # Sn = X_1 + ... + X_n, they chose 89 as conservative estimate after floor

    # if confidence_greater_than:
    #     return phi_inverse(prob, mu, var)
    # return phi_inverse(1 - prob, mu, var)

    quadratic_roots = solve_quadratic(a=-mu, b=-phi_inverse(prob, 0, 1, error_less_than=True) * math.sqrt(var), c=a)
    print("quad roots are ", quadratic_roots)
    return pow(quadratic_roots[0], 2), pow(quadratic_roots[1], 2)


def clt_n_greater_than(n=100, a=210, mu=2, sigma=2, greater_than=True):
    return phi((a - mu * n) / (sigma * math.sqrt(n)))


def solve_quadratic(a=1.0, b=-2.0, c=1.0):
    print("abc", a, b, c)
    plus_or_minus = math.sqrt(pow(b, 2) - 4 * a * c)
    return (-b + plus_or_minus) / (2 * a), (-b - plus_or_minus) / (2 * a)


# for normal approx to binomial, mu=p, s.d = sqrt(p*(1-p))
# P(Sn <= 21) = summation_k_0_to_21(nCk * pow(p, k)*pow(1-p, n-k)) = 0.8785 for n=36 p=0.5 k: 0 to 21
def binomial_approx(k=21, p=0.5, n=36):
    from counting.sim2 import comb
    return sum([comb(n, k_i) * pow(p, k_i) * pow(1 - p, n - k_i) for k_i in range(0, k + 1)])


def binomial_approx_point(k=21, p=0.5, n=36):
    from counting.sim2 import comb
    return comb(n, k) * pow(p, k) * pow(1 - p, n - k)


def binomial_de_moivre_laplace(x=19.0, n=36, p=0.5):
    mu = n * p
    var = n * p * (1 - p)
    sd = math.sqrt(var)
    # to get better value assume phi_between( ((x-0.5)-mu)/sd, ((x+0.5)-mu)/sd )
    return clt_phi_get_prob_binom(x + 0.5, n, p) - clt_phi_get_prob_binom(x - 0.5, n, p)


def binom_point_estimate(x=6, n=49, p=0.1):
    mu = n * p
    sd = math.sqrt(n * p * (1 - p))
    x1 = ((x - 0.5) - mu) / sd
    x2 = ((x + 0.5) - mu) / sd
    return phi_between(x1, x2, 0, 1)


def approx_equal(a, b):
    return math.isclose(a, b, rel_tol=1e-04)


if __name__ == '__main__':
    from counting.sim2 import comb

    print("test phi")
    print(phi(1))
    print(phi(0))
    print(phi(1, 1, 4))
    print(phi(1, var=2))
    print(phi(1, greater_than=True))
    print(solve_quadratic())
    assert (approx_equal(phi(1), 0.8413))
    assert (phi(0) == 0.5)
    assert phi(1, 1, 4), 0.5
    assert (approx_equal(phi(1, var=2), 0.7602))
    assert (approx_equal(phi(1, greater_than=True), 0.15865))
    assert (solve_quadratic()[0] == 1.0)
    assert (solve_quadratic()[1] == 1.0)

    print("\ntest lecture")
    print(clt_phi_get_prob())
    print(clt_phi_get_inverse_param())
    print(phi_inverse(0.05, 0, 1, error_less_than=True))
    print(clt_phi_get_n())
    print(solve_quadratic(-2, -2 * 1.645, 210))
    print(clt_n_greater_than())

    print("\nclt exercises")
    print(1 - clt_phi_get_prob(245, 2, 3, 100))
    print(clt_n_greater_than(49, 119, 2, 3))
    print(clt_phi_get_n(0.5, 2, 9, 128))

    print("\nbinomial approx")
    print(binomial_approx())
    print(sum([comb(36, k) * pow(0.5, 36) for k in range(0, 22)]))

    print(clt_phi_get_prob_binom(21, 36, 0.5))
    print(phi(21.0, 18.0, 9.0, greater_than=False))
    print(clt_phi_get_prob_binom(22, 36, 0.5))
    print(clt_phi_get_prob_binom(21.5, 36, 0.5))  # De Moivre Laplace CLT to binomial 0.8790 according to table

    print(phi_between(0.17, 0.5, 0, 1))
    print(binomial_de_moivre_laplace())
    print(binomial_approx_point(19, 0.5, 36))

    print("\n Exercises binomial")
    print(phi_between((5.5 - 4.9) / 2.1, (6.5 - 4.9) / 2.1, 0, 1))
    print(binom_point_estimate()) # phi(0.76) - phi(0.29) 0.1623
