import time, rich
from datetime import datetime

from upbitpy import Upbitpy

upbit = Upbitpy()

#buy_dic = {'KRW-ETH':3297222,'KRW-XRP':935, 'KRW-WAVES':33123, 'KRW-HUM':315, 'KRW-BTC':49600000}
#acc_dic = {'KRW-ETH':0.0,'KRW-XRP':5000.0, 'KRW-WAVES':0.0, 'KRW-HUM':300.0, 'KRW-BTC':0}
#ticker_list = list(buy_dic.keys())

while True:
    buy_dic = { line.split()[0] : [int(line.split()[1]), int(line.split()[2])] for line in open("input.txt") }
    ticker_list = list(buy_dic.keys())
    
    sum_profit_loss = 0
    tickers = upbit.get_ticker(ticker_list)
    curr_time = datetime.now().strftime("%H:%M:%S")
    rich.print('{}'.format(curr_time))
    print('{:^10}\t: {:^10}\t {:^10}\t ({:^7})\t [{:^10}]'.format('CODE', 'CURR', 'BUY', 'GAP', 'P/L'))
    print('-----------------------------------------------------------------------------')
    for ticker in tickers:
        code = ticker['market']
        curr_price = int(ticker['trade_price'])
        buy_price = buy_dic.get(code)[0] 
        step_price = curr_price-buy_price
        profit_loss = int(step_price*buy_dic.get(code)[1])
        print('{:10}\t: {:10,}\t {:10,}\t ({:=+7,})\t [{:=+10,}]'.format(code, curr_price, buy_price, step_price, profit_loss))
        sum_profit_loss = int(sum_profit_loss + profit_loss)
    print('-----------------------------------------------------------------------------')
    print('                                                            SUM : {:=+10,}'.format(sum_profit_loss))
    time.sleep(10)
#     clear_output(wait=True)
#     clear_output(wait=True)