

class Store:
    def __init__(self, name, list_of_products):
        self.name = name
        self.list_of_products = []
    
    def add_product(self, new_product):
        self.list_of_products.append(new_product)
        return self
        
    def sell_product(self, id):
        self.list_of_products.pop(id)
        
    def inflation(self, percent_increase): 
        for product in self.list_of_products:
            product.update_price(percent_increase, True)
        
    def set_clearance(self, category, percent_discount):
        for product in self.list_of_products:
            if product.category == category:
                product.update_price(percent_change, False)
            
class Products:
    def __init__(self, name, price, category): 
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if(is_increased): 
            self.price = self.price * (1 + percent_change) 
        else:
            self.price = self.price * (1 - percent_change)
    
    def print_info(self):
        print(f"The name of the product is {self.name}.\nThe category is {self.category}. \nThe price is {self.price}")

cupcake_store = Store("NYCcupcake", ["cupcake, birthdaycake"])   
cupcake = Products("cupcake", 5, "cake")
bdaycake = Products("birthdaycake",15, "cake")
cheesecake = Products("cheesecake", 25, "cake")

cupcake_store.add_product(cheesecake).add_product(bdaycake) 
print(cupcake_store.list_of_products[1].name)