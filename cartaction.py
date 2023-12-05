import json

def product_to_cart():
    print(f'Add a product success !')
    # if [pid == product['id'] for product in self._products]:
    #     print("No the product in database")


class CartAction:

    def __init__(self):
        self._cart = []
        self._products = None

    def product_out_cart(self, pid, username):
        # Remove it
        with open('Users.json', 'r') as file:
            user = json.load(file)
            user[username]["cart"].remove(pid)
        with open('Users.json', 'w') as file:
            json.dump(user, file, indent=4)



