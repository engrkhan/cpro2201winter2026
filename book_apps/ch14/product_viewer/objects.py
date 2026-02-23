from dataclasses import dataclass

@dataclass
class Product:
    # three attributes with default values
    name:str = ""                                 # attribute 1
    price:float = 0.0                             # attribute 2
    discountPercent:float = 0                     # attribute 3
    quantity:int  = 0                             # attribute 4
    subTotal:float = 0.0                          # attribute 5
    priceStr:str = ""                             # attribute 6


    
    # the initializer method that Python generates based on above
    def __init__(self, name="", quantity=0, price=0.0, discountPercent=0):
        self.name = name                          # attribute 1
        self.price = price                        # attribute 2
        self.discountPercent = discountPercent    # attribute 3
        self.quantity = quantity
    
    def getQuantitye(self):
        return self.quantity
    
    def getSubTotal(self):
        return (self.price - (self.price*self.discountPercent/100))*self.quantity
    
    # a method that uses two attributes to perform a calculation
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getPriceStr(self, country):
        priceStr = f"{self.price:.2f}"
        if country == "US":	
            priceStr += " USD"
        elif country == "DE":
            priceStr += " EUR"
        elif country == 'CA':
            priceStr += "CAD"
        return priceStr
