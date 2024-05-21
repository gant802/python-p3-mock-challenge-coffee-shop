from statistics import mean
    
class Coffee:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Coffee name={self.name}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Coffee already has a name")
        elif isinstance(name, str) and 3 <= len(name):
            self._name = name
        else : 
            raise Exception("Name must be a string that has 3 or more characters")

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        list_of_customers = [order.customer for order in Order.all if order.coffee == self]
        unique_set = set(list_of_customers)
        return list(unique_set)
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        price_list = [order.price for order in self.orders()]
        print(price_list)
        length = len(price_list)
        print(length)
        if length > 0:
            return sum(price_list) / length
        else:
            return 0 
        

class Customer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Customer name={self.name}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 16:
            self._name = name
        else : 
            raise Exception("Name must be a string between 1 and 15 characters")

        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        coffee_list = [order.coffee for order in Order.all if order.customer == self]
        unique_set = set(coffee_list)
        return list(unique_set)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.add_order(self)

    def __repr__(self):
        return f"<Order customer={self.customer} coffee={self.coffee} price={self.price}>"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, "_price"):
            raise Exception("Price can not be changed")
        elif isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else : 
            raise Exception("Price must be a float between 1.0 and 10.0")

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else : 
            raise Exception("Customer must be an instance of the Customer class")

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else : 
            raise Exception("Coffee must be an instance of the Coffee class")

    @classmethod
    def add_order(cls, order):
        cls.all.append(order)

