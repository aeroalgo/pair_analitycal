import numpy as np
from six.moves import xrange


def trade_spread(sell, buy, levels_ma_list, direction, depo, equity):
    komission = depo / 2 * 0.0019
    for dev in levels_ma_list[0]:
        for ma_per in levels_ma_list[1]:
            for matype in levels_ma_list[1][ma_per]:
                deviation_list = levels_ma_list[0][dev].tolist()
                ma_list = levels_ma_list[1][ma_per][matype].tolist()
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
                        entry_vol_ss = depo / 2 / sell[i]
                        entry_vol_bs = depo / 2 / buy[i]
                        count_trade += 2

                    if ma_list[i] * direction * -1 < 0 and count == 1:
                        count = 0
                        last_eq_ss = eq_sell_source1[-1]
                        last_eq_bs = eq_buy_source2[-1]

                cum_equity_trade = np.around(np.array(eq_sell_source1) + np.array(eq_buy_source2), 4)
                cum_equity = []
                if equity:
                    cum_equity = np.around(cum_equity_trade + np.array(equity), 4)
                    cum_equity = cum_equity.tolist()
                elif not equity:
                    cum_equity = cum_equity_trade.tolist()
                return cum_equity
