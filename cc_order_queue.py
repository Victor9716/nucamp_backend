import queue

class Queue:
    def __init__(self):
        self.items = []
        
class IceCreamShop:
    
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
        
    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Error:  Invalid flavor. please choose from available flavors.")
            return
        if not  1 <= scoops <= 3:
            print("Error: Scoops must be between 1 and 3")
            return
        
        print("Order Created!")
        order =  {"customer": customer, "flavor": flavor, "scoops": scoops}
        return self.orders.items.append(order)
        
    def show_all_orders(self):
        print("All pending Ice Cream Orders")
        for order in self.orders.items:
           
            print(order["customer"], "-", order["flavor"], "-", order["scoops"])
            
    def next_order(self):
        if len(self.orders.items) == 0:
            print("No orders Left")
            return None
        return  self.orders.items.pop(0)
           
           
            

            
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
        