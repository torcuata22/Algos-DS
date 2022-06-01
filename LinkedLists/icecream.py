class Queue:
    def __init__(self):
        self.items=[]
        
    def size(self):
            return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)
        

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
        
    def take_order(self, customer, flavors, scoops):
        if flavors not in self.flavors:
            print("Sorry, we don't have that flavor, please try again")
        elif scoops < 1 or scoops >3:
            print("Please choose between 1 and 3 scoops")
        else:
            print("Order created!")
            order = {"customer": customer, "flavor": flavors, "scoop": scoops}
            self.orders.enqueue(order)
    
    def show_all_orders(self):
        print("\n")
        print("Pending ice cream orders: ")
        for items in self.orders.items:
            print ("Customer: ",  items["customer"], "Flavor: ", items["flavor"], "Scoops: ", items["scoop"])
    
    def next_order(self):
        order_up = self.orders.dequeue()
        print("\n")
        print("Next order")
        print("Customer: ", order_up['customer'], "--Flavor: ", order_up['flavor'], "--Scoops: ",
              order_up['scoop'])
        
#Test code:
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
