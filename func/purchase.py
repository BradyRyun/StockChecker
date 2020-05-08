class Purchase:
    def __init__(self):
        self.purchaseStock = False

    def purchaseQuestion(self, p):
        if p.lower() == "y":
            purchaseStock = True
            print("We are buying stock today!")
        elif p.lower() == "n":
            purchaseStock = False
            print("No stocks will be bought today.")
        else:
            p = input("Please enter a valid response (Y/N): ")
            purchaseStock = Purchase.purchaseQuestion(self, p)
        return purchaseStock

# TODO Add actual stock purchasing functionality
# TODO Add in purchasing power variable
# Essentially, I want this to buy stocks where the Distribution is below the average (essentially the stocks in stocksUnderDistribution)
# Iterate through stocksUnderDistribution and buy 1 stock of the least distributed stock and move up one and do this until purchasing power cannot purchase more.

