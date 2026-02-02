from objects import Product

productsList = []

def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name}")
    print()

def show_product(product):
    w = 18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")
    print(f"{'Price:':{w}}{product.price:.2f}")
    print(f"{'Discount percent:':{w}}{product.discountPercent:d}%")
    print(f"{'Discount amount:':{w}}{product.getDiscountAmount():.2f}")
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print(f"{'Quantity:':{w}}{product.getQuantitye()}")
    print(f"{'Sub Total:':{w}}{product.getSubTotal():.2f}")
    print(f"Price with country:{w}{product.getPriceStr('CA')}")
    print()

def get_products():
    # return a tuple of Product objects
    
    productsList.append(Product("Stanley 13 Ounce Wood Hammer", 12.99, 62, 10))
    productsList.append(Product('National Hardware 3/4" Wire Nails', 5.06, 0, 5))
    productsList.append(Product('National Hardware 3/4" Wire Nails', 5.06, 0, 5))
    return (productsList[0],
            productsList[1],
            productsList[2])

def get_InvoiceTotal():
    # return a tuple of Product objects
    invoiceTotal = 0
    for p in productsList:
        invoiceTotal = invoiceTotal + p.getSubTotal()

    return invoiceTotal

def get_product(products):
    while True:
        try:
            number = int(input("Enter product number: "))
            if number < 1 or number > len(products):
                print("Product number out of range. Please try again.")
            else:
                return products[number-1]
        except ValueError:
            print("Invalid number. Please try again.")
        print()

def main():
    print("The Product Viewer program")
    print()
    
    products = get_products()
    show_products(products)
    print("The invoice total is \n")
    print(get_InvoiceTotal())

    choice = "y"
    while choice.lower() == "y":
        product = get_product(products)
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

    print("Bye!")
        

if __name__ == "__main__":
    main()
