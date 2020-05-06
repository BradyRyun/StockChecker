import robin_stocks
import numpy as np


username = input("Please enter your username: ")
password = input("Please enter your password: ")
robin_stocks.login(username, password)

# Build portfolio for program to use
mystocks = robin_stocks.build_holdings()

# Instantiating variables
items = len(list(mystocks.items()))
equity = 0
equityChange = 0
highPerformers = []
lowPerformers = []
stocksToPurchase = []
highPerformersAndUnderDistributionStocks = []
arr = []
distributionAverage = 100 / items

for key, value in mystocks.items():
    arr = np.array(list(value.values())).flatten()
    # Summing equity total
    equity = float(arr[3]) + float(equity)
    # Summing equityChange
    equityChange = float(arr[4]) + float(equityChange)

# Calculating average change to compare each stock's performance to
equityAverageChange = float(equityChange) / float(items)


# Testing each stock against averages
for key, value in mystocks.items():
    arr = np.array(list(value.values())).flatten()
    if float(arr[4]) > float(equityAverageChange):
        highPerformers.append(key)
    else:
        lowPerformers.append(key)
    if float(arr[10]) < float(distributionAverage):
        stocksToPurchase.append(key)
for i in stocksToPurchase:
    highPerformersAndUnderDistributionStocks = [value for value in stocksToPurchase if value in highPerformers]

print("Total equity: ")
print("$" + str(round(equity, 2)))
print("Highest performers: ")
print(highPerformers)
print("Lowest performers: ")
print(lowPerformers)
print("Distribution average: ")
print(str(round(distributionAverage, 2)))
if len(highPerformersAndUnderDistributionStocks) != 0:
    print(highPerformersAndUnderDistributionStocks)
else:
    print("There were no high performing stocks under the current distribution")
    print("Stocks under distribution percentage average: ")
    print(stocksToPurchase)




