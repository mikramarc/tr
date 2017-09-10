import numpy as np
from scipy.signal import argrelextrema
from dummy_api import DummyData, DummyWallet
from gui import TradingGui
import time

def running_mean_fast(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

def average_filter(data, n):
    num_of_samples = len(data)
    if n >= num_of_samples:
        n = int(round(num_of_samples/2))-1
    data_filtered = np.zeros(num_of_samples)

    for i in range(n):
        for j in range(-i, i+1):
            data_filtered[i] += data[i+j]
        data_filtered[i] /= 2*i+1

    for i in range(n, num_of_samples-n):
        for j in range(-n, n+1):
            data_filtered[i] += data[i+j]
        data_filtered[i] /= 2*n+1

    for i in range(num_of_samples-n, num_of_samples):
        for j in range(-(num_of_samples-(i+1)), (num_of_samples-(i+1))+1):
            data_filtered[i] += data[i+j]
        data_filtered[i] /= 2*(num_of_samples-(i+1))+1

    return data_filtered

btc_euro = DummyData('data/btceurEUR.csv')
wallet = DummyWallet()
gui = TradingGui(100)
data_history = np.zeros(100)
current_price = 0

while current_price != -1:
    current_price = btc_euro.get_price()
    data_history = np.append(data_history, current_price)
    data_history_filtered = average_filter(data_history, 10)

    # gui.plot_data_history(data_history)
    gui.plot_data_history(data_history_filtered, 'r-')


# btc_euro_data_filtered = running_mean_fast(btc_euro_data[:, 1], 200)
# maxima = argrelextrema(btc_euro_data_filtered, np.greater, 0, 100)
# minima = argrelextrema(btc_euro_data_filtered, np.less, 0, 100)
#
# print btc_euro_data_filtered[maxima]
#
# plt.plot(btc_euro_data_filtered)
# plt.scatter(maxima, btc_euro_data_filtered[maxima], color='red')
# plt.scatter(minima, btc_euro_data_filtered[minima], color='blue')
# plt.ylabel('some numbers')
# plt.show()