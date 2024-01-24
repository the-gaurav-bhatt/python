# Create a class bill. Bill should contain date, customer name and details of # of items - name,
# rate, quantity, total amount. Make a bill and display it.
class Bill:
    def __init__(self,cname,date):
        self.cname = cname
        self.date = date
        self.items = []

    def additem(self,iname,quantity,rate):
        self.items.append({
            'Item_Name' : iname,
            "Quantity":quantity,
            "Rate":rate,
            "Total":rate*quantity
        })
    def finalBill(self):
        print("INVOICE")
        print("Customer Name :" + self.cname)
        print("Item Name \t\tQuantity\t\trate\t\tTotal")
        for item in self.items:
            message = f"{item['Item_Name']}\t\t{item['Quantity']}\t\t {item['Rate']}\t\t{item['Total']}"
            print(message)

Gaurav = Bill ("Gaurv","22-09-23")
Gaurav.additem("Chicken",2,100)
Gaurav.finalBill()




