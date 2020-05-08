class Purchase:
    def purchaseQuestion(p):
        purchaseStock = False
        if p.lower() == "y":
            purchaseStock = True
        elif p.lower() == "n":
            purchaseStock = False
        else:
            p = input("Please enter a valid response (Y/N): ")
            purchaseStock = Purchase.purchaseQuestion(p)
        return purchaseStock
