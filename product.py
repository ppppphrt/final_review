import json


class Product:
    def __init__(self):
        data = [
            {
                "id": 1,
                "name": "Atomic Habit",
                "price": 790,
                "stock": 11
            },
            {
                "id": 2,
                "name": "The magic of thinking big",
                "price": 350,
                "stock": 6
            },
            {
                "id": 3,
                "name": "Ask and it is given",
                "price": 690,
                "stock": 9
            },
            {
                "id": 4,
                "name": "Emotional intelligence",
                "price": 590,
                "stock": 13
            },
            {
                "id": 5,
                "name": "Think and grow rich",
                "price": 250,
                "stock": 19
            }
        ]
        try:
            with open('Product.json', 'r') as file:
                self._products = json.load(file)  # Load data products from Database/Product.json
        except FileNotFoundError:
            with open("Product.json", "w") as file:
                json.dump(data, file, indent=4)

    def products(self, product_id=None):

        if product_id is None:
            return self._products

        uniq_pid = sorted(set(product_id))  # Drop duplicate then sort ascending
        products_output = []
        for p in self._products:  # Interate products object data
            if p['id'] == uniq_pid[0]:  # If id from interate is equal `uniq_pid` (^ that ascending before)
                uniq_pid.pop(0)  # Remove first element of `uniq_pid`
                products_output.append(p)
            if len(uniq_pid) == 0:  # If no element in `uniq_pid` so return data products
                return products_output
        print("Product_id is incorrect, Please check again!")

    def show_products(self):
        print("\n\n")
        print("Table: Product")
        print(f"Number of products: {len(self._products)}")
        print("------------------------------------------------------------------------------------")
        print("   ID                 Name                         Price                 Stock")
        print("------------------------------------------------------------------------------------")
        for product in self._products:
            print("{pid:5}{name:^40}{price:>11,.2f}{stock:>21}".format(pid=product['id'], name=product['name'],
                                                                       price=float(product['price']),
                                                                       stock=product['stock']))
        print("---------------------------------------------------------------------------------\n\n")

    def update_stock(self, product):
        with open('Product.json', 'r') as jf:
            stock = json.load(jf)
            for i in stock:
                if i['id'] == product:
                    i['stock'] -= 1
                    break
            with open('Product.json', 'w') as jsonFile:
                json.dump(stock, jsonFile, indent=4)
