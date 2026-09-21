class StockItem:
    def __init__(self, name : str, quantity : int):
        self.name = name
        self.quantity = quantity
    
        
class Stock:
    def __init__(self):
        self.items = []
        
    def add_product(self, product: StockItem):
        self.items.append(product)
        
    def get_products(self, name):
        for items in self.items:
            if items.name == name:
                return items
        return None   
        
        
    def reduce_quantity(self, product_name : str, quantity_to_remove: int):
        item = self.get_products(product_name)
        if not item:
            raise ValueError(f"Product {product_name} not found")
        
        if item.quantity >= quantity_to_remove:
            item.quantity -= quantity_to_remove
            
        else:
            raise ValueError(f"Product {product_name} is not enough in stock")
        