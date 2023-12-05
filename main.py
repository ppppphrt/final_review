from ShoppingClass.cartaction import product_to_cart
from ShoppingClass.shopping import Shopping

user = Shopping()  # Create the object.

if __name__ == '__main__':

    print("\n")
    print('WELCOME TO OUR BOOK SHOP')
    print("\n")
    choice = input('(r) for Register or (l) for login: ')
    while True:
        if choice == 'l':
            user_1 = input('Enter your username: ')
            pas_1 = input('Enter your password: ')
            user.login(user_1, pas_1)
            break
        elif choice == 'r':
            new_name = input('Enter your name: ')
            user_1 = input('Create your username: ')
            pas_1 = input('Create your password: ')
            user.register(user_1, new_name, pas_1)
            print(f'Register success !\nWelcome {user_1}\n')
            break

        else:
            print('Please input again.')
            choice = input('(r) for Register or (l) for login: ')

    user.show_products()  # Display all products in the market
    # Add products to my cart
    while True:
        product = int(input('Please enter id of your book or 888 to quit: '))
        # user.buy(product,product)
        # user.product_to_cart(product)
        if product == 888:
            break
        else:
            user.buy_to_cart(user_1, product)
            product_to_cart()
            user.update_stock(product)
            # user.show_buy(user_1)

    # user.show_products()  # Display all products in the market
    user.show_cart(user_1)  # Display all products in my cart

    # Drop products from my cart
    while True:
        remove_product = int(input('Please enter id of your book to remove or 0 to quit: '))

        if remove_product == 0:
            break

        elif remove_product != 0:
            user.product_out_cart(remove_product, user_1)
            remove_product = int(input('Please enter id of your book to remove or 0 to quit: '))
            print('Remove a product success !')
            break

    # Display data

    user.show_cart(user_1)
