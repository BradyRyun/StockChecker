class Purchase:
    def __init__(self):
        print("Purchase object started")

    def purchaseQuestion(p):
        purchaseStock = False
        if p.lower() == "y":
            purchaseStock = True
        elif p.lower() == "n":
            purchaseStock = False
        else:
            p = input("Please enter a valid response (Y/N): ")
            Purchase.purchaseQuestion(p)
        return purchaseStock
