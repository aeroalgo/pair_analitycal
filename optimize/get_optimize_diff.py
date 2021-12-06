import talib
import numpy as np
import pandas as pd
from six.moves import xrange
from metrics.get_metrics import get_determination_coef, get_median
from view.chart import get_chart
import matplotlib.pyplot as plt


def get_moving(ma_param, spread, ma_num, ma_period_opt):
    ma_dict = {}
    if ma_period_opt == 'all':
        for ma_period in ma_param:
            ma_period_dict = {}
            ma_type = {
                '6': talib.DEMA(spread, ma_period),
                '1': talib.EMA(spread, ma_period),
                '5': (3 * talib.WMA(spread, ma_period) - 2 * talib.SMA(spread, ma_period)),
                '4': talib.KAMA(spread, ma_period),
                '0': talib.SMA(spread, ma_period),
                '8': talib.T3(spread, ma_period),
                '7': talib.TEMA(spread, ma_period),
                '2': talib.WMA(spread, ma_period)
            }
            if ma_num == 'all':
                for type_ma in ma_type:
                    ma = ma_type[type_ma]
                    spread_ind = spread - ma
                    ma_period_dict[type_ma] = spread_ind
                    ma_dict[ma_period] = ma_period_dict
            elif ma_num != 'all':
                ma = ma_type[ma_num]
                spread_ind = spread - ma
                ma_period_dict[ma_num] = spread_ind
                ma_dict[ma_period] = ma_period_dict
        return ma_dict
    elif ma_period_opt != 'all':
        ma_period_dict = {}
        ma_type = {
            '6': talib.DEMA(spread, ma_period_opt),
            '1': talib.EMA(spread, ma_period_opt),
            '5': (3 * talib.WMA(spread, ma_period_opt)) - 2 * talib.SMA(spread, ma_period_opt),
            '4': talib.KAMA(spread, ma_period_opt),
            '0': talib.SMA(spread, ma_period_opt),
            '8': talib.T3(spread, ma_period_opt),
            '7': talib.TEMA(spread, ma_period_opt),
            '2': talib.WMA(spread, ma_period_opt)
        }
        if ma_num != 'all':
            ma = ma_type[ma_num]
            spread_ind = spread - ma
            ma_period_dict[ma_num] = spread_ind
            ma_dict[ma_period_opt] = ma_period_dict
            return ma_dict
        elif ma_num == 'all':
            for type_ma in ma_type:
                ma = ma_type[type_ma]
                spread_ind = spread - ma
                ma_period_dict[type_ma] = spread_ind
                ma_dict[ma_period_opt] = ma_period_dict
            return ma_dict


def trade_spread(sell, buy, levels_ma_list, direction, depo, equity, numlevel, lot_ss, lot_bs):
    global data_sort
    opt_value_param = {
        'Profit': [],
        'R2': [],
        'DD': [],
        'RF': [],
        'P/L%': [],
        'MA Period': [],
        'MA Type': [],
        'Volatility': [],
        'Dev': []
    }
    equity_list = []
    profit_p = 0
    profit_m = 0
    komission = depo / 2 * 0.0025
    for dev in levels_ma_list[0]:
        for vola in levels_ma_list[1]:
            for ma_per in levels_ma_list[1][vola]:
                for matype in levels_ma_list[1][vola][ma_per]:
                    deviation_list = levels_ma_list[0][dev].tolist()
                    ma_list = levels_ma_list[1][vola][ma_per][matype].tolist()
                    entry_price_ss = 0
                    entry_price_bs = 0
                    entry_vol_ss = 0
                    entry_vol_bs = 0
                    last_eq_ss = 0
                    last_eq_bs = 0
                    max_eq_value = 0
                    dd = 0
                    eq_sell_source1 = [0]
                    eq_buy_source2 = [0]
                    count = 0
                    count_trade = 0
                    for i in xrange(len(deviation_list)):
                        if not equity:
                            if eq_sell_source1[i] + eq_buy_source2[i] > max_eq_value:
                                max_eq_value = eq_sell_source1[i] + eq_buy_source2[i]
                            dd1 = (eq_sell_source1[i] + eq_buy_source2[i]) - max_eq_value

                            if dd1 < dd:
                                dd = dd1
                        if equity:
                            if eq_sell_source1[i] + eq_buy_source2[i] + equity[i] > max_eq_value:
                                max_eq_value = eq_sell_source1[i] + eq_buy_source2[i] + equity[i]
                            dd1 = (eq_sell_source1[i] + eq_buy_source2[-1] + equity[i]) - max_eq_value

                            if dd1 < dd:
                                dd = dd1
                        if count == 0:
                            eq_sell_source1.append(eq_sell_source1[-1])
                            eq_buy_source2.append(eq_buy_source2[-1])
                        if count == 1:
                            eq_sell_source1.append(
                                (entry_price_ss - sell[i]) * entry_vol_ss - komission + last_eq_ss)
                            eq_buy_source2.append(
                                (buy[i] - entry_price_bs) * entry_vol_bs - komission + last_eq_bs)
                        if ma_list[i] * direction * -1 > deviation_list[i] and count == 0:
                            count = 1
                            entry_price_ss = sell[i]
                            entry_price_bs = buy[i]
                            if direction == 1:
                                entry_vol_ss = lot_ss[i] * vola
                                entry_vol_bs = lot_bs[i]
                            if direction == -1:
                                entry_vol_ss = lot_ss[i]
                                entry_vol_bs = lot_bs[i] * vola
                            count_trade += 2

                        if ma_list[i] * direction * -1 < 0 and count == 1:
                            count = 0
                            last_eq_ss = eq_sell_source1[-1]
                            last_eq_bs = eq_buy_source2[-1]
                        if i == round(len(deviation_list)) / 2 and eq_sell_source1[-1] + eq_buy_source2[-1] < 0:
                            break

                    cum_equity_trade = np.around(np.array(eq_sell_source1) + np.array(eq_buy_source2), 4)
                    cum_equity = []
                    if cum_equity_trade[-1] > 0:
                        profit_p += 1
                    elif cum_equity_trade[-1] < 0:
                        profit_m += 1
                    if cum_equity_trade[-1] > 0 and dd < 0:
                        if equity:
                            cum_equity = np.around(cum_equity_trade + np.array(equity), 4)
                            cum_equity = cum_equity.tolist()
                        elif not equity:
                            cum_equity = cum_equity_trade.tolist()

                        median = get_median(cum_equity)
                        determination_coef = get_determination_coef(median, cum_equity)

                        opt_value_param['Profit'].append(cum_equity[-1])
                        opt_value_param['R2'].append(round(determination_coef, 4))
                        opt_value_param['DD'].append(round(dd, 4))
                        opt_value_param['RF'].append(round(cum_equity[-1] / dd * -1, 4))
                        opt_value_param['P/L%'].append(round(cum_equity_trade[-1] / count_trade * 2 / (depo / 100), 2))
                        opt_value_param['MA Period'].append(int(ma_per))
                        opt_value_param['MA Type'].append(int(matype))
                        opt_value_param['Volatility'].append(float(vola))
                        opt_value_param['Dev'].append(float(dev))
                        equity_list.append(cum_equity)
    if numlevel == 1:
        data_sort = pd.DataFrame(opt_value_param).sort_values('Profit', ascending=False)
    if numlevel == 2:
        data_sort = pd.DataFrame(opt_value_param).sort_values('RF', ascending=False)
    data_sort = data_sort[data_sort['P/L%'] > 0.15]
    data_sort = data_sort[data_sort['P/L%'] < 0.9]
    data_sort = data_sort.drop(data_sort.index[10:])
    data_sort = pd.DataFrame(data_sort).sort_values('P/L%', ascending=False)
    data_sort = data_sort.drop(data_sort.index[5:])
    data_sort = pd.DataFrame(data_sort).sort_values('R2', ascending=False)
    data_sort = data_sort.drop(data_sort.index[1:])
    data_sort['% Вad result'] = [np.around(profit_m / (profit_m + profit_p) * 100, 2)]
    data_sort_dict = data_sort.to_dict(orient='records')
    try:
        data_param_eq = [data_sort_dict, equity_list[data_sort.index[0]]]
    except IndexError:
        data_param_eq = [data_sort_dict, []]
    return data_param_eq


def trade_spread_rough(sell, buy, indicator, kat, level, direction, depo, lot_ss, lot_bs):
    sell_source1 = []
    buy_source2 = []
    lot1 = []
    lot2 = []
    count = 0
    komission = depo * 0.0012
    trade = 0
    for i in range(len(sell)):
        if indicator[i] * direction * -1 > kat[i] * level and count == 0:
            count += 1
            sell_source1.append(sell[i])
            buy_source2.append(buy[i])
            lot1.append(lot_ss[i])
            lot2.append(lot_bs[i])
            trade += 2
        if indicator[i] * direction * -1 < 0 and count == 1:
            count = 0
            sell_source1.append(sell[i])
            buy_source2.append(buy[i])
            lot1.append(lot_ss[i])
            lot2.append(lot_bs[i])
    profit = 0
    # p1 = [0]
    # p2 = [0]
    for i in range(0, len(sell_source1), 2):
        volume1 = lot1[i]
        volume2 = lot2[i]
        try:
            x = (sell_source1[i] - sell_source1[i + 1]) * volume1 - komission
            y = (buy_source2[i + 1] - buy_source2[i]) * volume2 - komission
            # p1.append(p1[-1] + x)
            # p2.append(p2[-1] + y)
            profit += x + y
        except IndexError:
            break
            # print(buy_source2[i], volume2)
            # print(sell_source1[i], volume1)
    # p1 = np.array(p1)
    # p2 = np.array(p2)
    # p3 = p1 + p2
    # plt.title(direction)
    # plt.plot(p3)
    # plt.show()

    return profit
