from django.conf import settings
from Products.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        #def __init__(self, request):: The constructor method is called when an instance of the class is created. It initializes the cart by checking the session for an existing cart. If a cart doesn't exist in the session, it creates an empty one.
        #self.session = request.session: Stores the Django session object in an instance variable for later use.
        #cart = self.session.get(setting.CART_SESSION_ID): Retrieves the cart from the session using the CART_SESSION_ID defined in Django settings. 

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            #If the cart doesn't exist, it initializes it as an empty dictionary.

        self.cart = cart
        #self.cart = cart: Stores the cart in the instance variable for easy access.

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
            #The method iterates over the product_id keys of the cart and retrieves the corresponding Product object from the database, associating it with the cart item.

            # using the __iter__ method the Cart class will be iterable. Each iteration over the cart will fetch the corresponding Product object from the database and associate it with the cart item. This can be useful if you want to access both the cart items and their associated products in a loop.

        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity']) # / 100
           #Here, it looks like you're calculating the total price for each item in the cart. Let's break it down:

# item['product']: This seems to be the product associated with the current item in the cart.
# item['product'].price: This is the price of the product.
# item['quantity']: This is the quantity of the product in the cart.
# The total price is calculated as the product of the price and the quantity. The result is then converted to an integer using int(). It's important to note that the comment mentions a division by 100, but it's currently commented out (# / 100). If you uncomment it, it would mean dividing the calculated total price by 100.

            yield item
            # Finally, the yield item statement suggests that this code is part of a generator function. Generators are a way to create iterators in Python. In this case, it seems that the code is part of a method that yields items, possibly for further processing or displaying in a template.

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    #def __len__(self):: This method returns the total number of items in the cart by summing the quantities of all cart items.
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        #def save(self):: Saves the current state of the cart to the session.

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        #adds the product to the cart and makes sure product is a string

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}
            #checks if the product is not already in the cart. it adds the product with an initial quantity

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)
            #If update_quantity is set to True, it updates the quantity of the product.

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
                # If the quantity becomes zero, it removes the product from the cart.

        self.save()


    def remove(self, product_id):
        if product_id in self.cart:
            #checks if product is in the cart
            del self.cart[product_id]
            #if yes then it removes the product
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
        #When dealing with dictionaries, always use square brackets for accessing and modifying values associated with keys. Parentheses are used for function calls and defining tuples, while curly brackets are used for defining sets and dictionaries. Understanding the context and purpose of each bracket type will help you use the correct syntax in different situations.


    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['product'].price * item ['quantity' ] for item in self.cart.values()))
    
    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None
    
    
