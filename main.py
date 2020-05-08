import robin_stocks
import numpy as np


username = input("Please enter your username: ")
password = input("Please enter your password: ")
purchasing = input("Are we purchasing stock today? Y/N: ")

if purchasing.lower() == "y":
    purchaseStock = True
elif purchasing.lower() != "n":
    purchaseStock = False
else:
    purchaseStock = False

robin_stocks.login(username, password)

# Build portfolio for program to use
mystocks = robin_stocks.build_holdings()

# Instantiating variables
items = len(list(mystocks.items()))
equity = 0
equityChange = 0
highPerformers = []
lowPerformers = []
nestedHigh = []
nestedLow = []
nestedDist = []
distroList = []
stocksUnderDistribution = []
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
        nestedHigh.append(key)
        nestedHigh.append(str(round(float((arr[4])), 2)) + "%")
    else:
        nestedLow.append(key)
        nestedLow.append(str(round(float((arr[4])), 2)) + "%")
    if float(arr[10]) < float(distributionAverage):
        nestedDist.append(key)
        nestedDist.append(str(round(float((arr[10])), 2)) + "%")
        distroList.append(key)

# Checks if a stock is under the average distribution and is a high performing stock.
for i in distroList:
    highPerformersAndUnderDistributionStocks = [value for value in distroList if value in highPerformers]

# Adding lists inside of lists
highPerformers.append(nestedHigh)
lowPerformers.append(nestedLow)
stocksUnderDistribution.append(nestedDist)

print("Total equity: ")
print("$" + str(round(equity, 2)))
print("Highest performers: ")
print(highPerformers)
print("Lowest performers: ")
print(lowPerformers)
if len(highPerformersAndUnderDistributionStocks) > 0:
    print(highPerformersAndUnderDistributionStocks)
else:
    print("There were no high performing stocks under the current distribution")
    print("Stocks under distribution percentage average: ")
    print(stocksUnderDistribution)




