import matplotlib.pyplot as plt

class TradingGui(object):
    def __init__(self, plotting_window):
        plt.axis([0, plotting_window, 0, 1000])
        plt.ion()
        self.res = plt.plot([])
        self.plotting_window = plotting_window

    def plot_data_history(self, data_history, plot_style='k-'):
        for handle in self.res:
            handle.remove()
        if len(data_history) < self.plotting_window:
            self.res = plt.plot(data_history, plot_style)
        else:
            self.res = plt.plot(data_history[len(data_history)-self.plotting_window:-1], plot_style)
        plt.pause(0.0001)
        return self.res
