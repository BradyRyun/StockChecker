import robin_stocks
from func.info import Info
from func.purchase import Purchase

username = input("Please enter your username: ")
password = input("Please enter your password: ")
purchasing = input("Are we purchasing stock today? Y/N: ")


buyStock = Purchase.purchaseQuestion(purchasing)

if(buyStock == True):
    print("We are buying stock today!")
else:
    print("No stocks will be bought today.")
robin_stocks.login(username, password)

# Build portfolio for program to use
print("Obtaining information from Robinhood. Please wait.")
info = Info()

print("Total equity: ")
print("$" + str(round(info.equity, 2)))
print("Highest performers: ")
print(info.highPerformers)
print("Lowest performers: ")
print(info.lowPerformers)

# TODO Add in purchasing power variable
# Essentially, I want this to buy stocks where the Distribution is below the average (essentially the stocks in stocksUnderDistribution)
# Iterate through stocksUnderDistribution and buy 1 stock of the least distributed stock and move up one and do this until purchasing power cannot purchase more.
