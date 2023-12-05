import json


class User:
    def __init__(self):
        self._userId = 0
        self._name = ""
        self._cart = []
        self.username = ""

    data = {
        "user1": {
            "id": 1,
            "name": "m",
            "password": "1234",
            "cart": [

            ]
        },
        "user2": {
            "id": 2,
            "name": "n",
            "password": "2345",
            "cart": [

            ]
        },
        "ccc": {
            "id": 3,
            "name": "ccccc",
            "password": "12345",
            "cart": []
        },
        "cchef": {
            "id": 4,
            "name": "ccc",
            "password": "1111",
            "cart": [

            ]
        },
        "phavida": {
            "id": 5,
            "name": "ppphrt",
            "password": "120946",
            "cart": []
        },
        "mue": {
            "id": 6,
            "name": "nongmue",
            "password": "2222",
            "cart": []
        }
    }
    try:
        with open('Users.json', 'r') as file:
            user = json.load(file)  # Load data products from Database/Product.json
    except FileNotFoundError:
        with open("Users.json", "w") as file:
            json.dump(data, file, indent=4)

    def login(self, username, password):
        while True:
            with open('Users.json', 'r') as file:
                user = json.load(file)

            if username in user:
                if user[username]["password"] == password:
                    self._userId = user[username]['id']
                    self._name = user[username]['name']
                    self._cart = user[username]['cart']
                    self.username = username
                    print(f'Login success !\n\nWelcome {self._name}\n\n')
                    break
                else:
                    print('Username or Password is incorrect')
                    print('Please enter again.')
                    input('Enter your username: ')
                    input('Enter your password: ')
                    break

    def register(self, username, name, password):
        try:
            with open('Users.json', 'r') as file:
                user = json.load(file)

            new_user = {
                username: {"id": len(user) + 1,
                           "name": name,
                           "password": password,
                           "cart": []
                           }

            }


        except FileNotFoundError:
            with open('Users.json', 'w') as file:
                user = {
                    username: {"id": 1,
                               "name": name,
                               "password": password,
                               "cart": []

                               }

                }
                json.dump(user, file, indent=4)

        else:
            user.update(new_user)
            with open('Users.json', 'w') as file:
                json.dump(user, file, indent=4)

    def buy_to_cart(self, username, id):
        with open('Users.json', 'r') as file:
            user = json.load(file)
            user[username]["cart"].append(id)
        with open('Users.json', 'w') as file:
            json.dump(user, file, indent=4)

    def show_buy(self, username):
        with open('Users.json', 'r') as file:
            user = json.load(file)
            return user[username]["cart"]
