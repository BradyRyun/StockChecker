from func.info import Info
from func.purchase import Purchase

username = input("Please enter your username: ")
password = input("Please enter your password: ")
purchasing = input("Are we purchasing stock today? Y/N: ")

p = Purchase()
buyStock = Purchase.purchaseQuestion(p, purchasing)

# Build portfolio for program to use
print("Obtaining information from Robinhood. Please wait.")
info = Info(username, password)

print("Portfolio Market Value: ")
print("$" + str(round(info.equity, 2)))
print("Highest performers: ")
print(info.highPerformers)
print("Lowest performers: ")
print(info.lowPerformers)

if len(info.highPerformersAndUnderDistributionStocks) > 0:
    print(info.highPerformersAndUnderDistributionStocks)
else:
    print("There were no high performing stocks under the current distribution")
    print("Stocks under distribution percentage average: ")
    print(info.stocksUnderDistribution)

