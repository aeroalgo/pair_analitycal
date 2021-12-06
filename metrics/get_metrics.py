from sklearn.linear_model import LinearRegression
import numpy as np


def dd_abs(cm_eq):
    dd = []
    max = 0
    for i in cm_eq:
        if i > max:
            max = i
        dd.append(i - max)
    return dd


def dd_percent(cm_eq, q_algo, size, leverage):
    max = 0
    dd = []
    for i in cm_eq:
        if i > max:
            max = i
        dd.append((i - max) * 100 / (q_algo * size) * leverage)
    return dd


def profit_per_day(cm_eq, q_algo, size, leverage):
    profit = []
    for i in range(len(cm_eq) - 2016):
        profit.append((cm_eq[i + 2016] - cm_eq[i]) / 2016 * 288 * 100 / ((q_algo * size) / leverage))
    return profit


def get_median(equity):
    y = max(equity) / len(equity)
    x = [0]
    for i in range(len(equity) - 1):
        x.append(x[-1] + y)
    x = np.array(x).reshape((-1, 1))
    return x


def get_determination_coef(median, common_equity):
    model = LinearRegression().fit(median, common_equity)
    r_sq = model.score(median, common_equity) ** 4
    return r_sq


def profit_pct(profit, qalgo, size, liverage):
    profitpct = []
    for i in profit:
        profitpct.append(i * 100 / (qalgo * size / liverage))
    return profitpct
