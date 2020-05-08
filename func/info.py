import numpy as np
import robin_stocks


class Info:
    def __init__(self):
        # Instantiating variables
        self.mystocks = robin_stocks.build_holdings()
        self.items = len(list(self.mystocks.items()))
        self.equity = 0
        self.equityChange = 0
        self.highPerformers = []
        self.lowPerformers = []
        self.nestedHigh = []
        self.nestedLow = []
        self.nestedDist = []
        self.distroList = []
        self.stocksUnderDistribution = []
        self.highPerformersAndUnderDistributionStocks = []
        self.arr = []
        self.distributionAverage = 100 / self.items
        for key, value in self.mystocks.items():
            arr = np.array(list(value.values())).flatten()
            # Summing equity total
            equity = float(arr[3]) + float(self.equity)
            # Summing equityChange
            equityChange = float(arr[4]) + float(self.equityChange)

        # Calculating average change to compare each stock's performance to
        equityAverageChange = float(self.equityChange) / float(self.items)

        # Testing each stock against averages
        for key, value in self.mystocks.items():
            arr = np.array(list(value.values())).flatten()
            if float(arr[4]) > float(equityAverageChange):
                self.nestedHigh.append(key)
                self.nestedHigh.append(str(round(float((arr[4])), 2)) + "%")
            else:
                self.nestedLow.append(key)
                self.nestedLow.append(str(round(float((arr[4])), 2)) + "%")
            if float(arr[10]) < float(self.distributionAverage):
                self.nestedDist.append(key)
                self.nestedDist.append(str(round(float((arr[10])), 2)) + "%")
                self.distroList.append(key)

        # Checks if a stock is under the average distribution and is a high performing stock.
        for i in self.distroList:
            highPerformersAndUnderDistributionStocks = [value for value in self.distroList if
                                                        value in self.highPerformers]

        # Adding lists inside of lists
        self.highPerformers.append(self.nestedHigh)
        self.lowPerformers.append(self.nestedLow)
        self.stocksUnderDistribution.append(self.nestedDist)

        if len(self.highPerformersAndUnderDistributionStocks) > 0:
            print(self.highPerformersAndUnderDistributionStocks)
        else:
            print("There were no high performing stocks under the current distribution")
            print("Stocks under distribution percentage average: ")
            print(self.stocksUnderDistribution)
