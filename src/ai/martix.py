import math


def benfit(total, rate, year):
    return total*math.pow(1+rate, year)


def year_benfit(pre_year, n, rate):
    if n == 1:
        return pre_year*(1+rate)
    else:
        return (year_benfit(pre_year, n-1, rate)+pre_year)*(1+rate)


print(benfit(150000, 0.05, 10))

for i in range(1, 6):
    print(i, year_benfit(30000, i, 0.048))
