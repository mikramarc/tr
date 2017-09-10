import numpy as np
import csv


class DummyData(object):
    def __init__(self, file):
        self.data = []
        self.load_data(file)

    def load_data(self, file):
        with open(file, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.data.append(map(float, row))

        self.data = np.array(self.data)
        self.data = self.data[:, 1]

    def get_price(self):
        try:
            current_value = self.data[0]
            self.data = np.delete(self.data, 0)
            return current_value
        except:
            print "No data available"
            return -1

class DummyWallet(object):
    def __init__(self):
        self.current_balance = 1000
        self.balance_history = []
