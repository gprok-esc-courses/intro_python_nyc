class Invoice:
    def __init__(self, sn, customer):
        if isinstance(sn, int):
            self.sn = sn 
        else:
            print("Error, invalid serial number")
            self.sn = None
        self.items = {}
        self.customer = customer 

    def add_item(self, item_name, item_price):
        if isinstance(item_price, float):
            self.items[item_name] = item_price
        else:
            print("Wrong price type")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total = total + self.items[item]
        return total

    def __str__(self):
        t = self.calculate_total()
        s = f"{self.sn}. Customer: {self.customer}. Total: {t}"
        return s


a = Invoice(1, "Peter")
b = Invoice(2, "Mike")

a.add_item('keyboard', 45.2)
a.add_item('mouse', 100.3)

b.add_item('keyboard', 198.3)
b.add_item('monitor', 150.0)

print(a)
print(b)