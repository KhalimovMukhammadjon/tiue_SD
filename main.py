import user

users = []

category_product = {
    'Water': ['Sprite 1L', 'Coca Cola 1.5L', 'Coca Cola 0.5L', 'Fanta 1L', 'Fanta 1.5L'],
    'Dairy': ['Milk Lactel 3.2% 1L', 'Kefir Pure Milky 3.2% 920g', 'Yogurt Pure Milky 2.5% 330g',
              'Butter Light butter 72% 1kg'],
    'Meat': ['Salmon Fly Fish 350g', 'Rostov Beef 1kg', 'Sausage Rozmetov 500g', 'Beef Liver 1kg'],
    'Chocolates': ['Chocolate Pobeda 57% dark 100g', 'Chocolate Millenium Riviera', 'Twix 55g',
                   'Millenium Milk Porous 90g']
}

product_price = {
    'Sprite 1L': 7490,
    'Coca Cola 1.5L': 9990,
    'Coca Cola 0.5L': 4990,
    'Fanta 1L': 7490,
    'Fanta 1.5L': 9990,
    'Milk Lactel 3.2% 1L': 9490,
    'Kefir Pure Milky 3.2% 920g': 11490,
    'Yogurt Pure Milky 2.5% 330g': 6490,
    'Butter Light butter 72% 1kg': 31990,
    'Salmon Fly Fish 350g': 96490,
    'Rostov Beef 1kg': 83990,
    'Sausage Rozmetov 500g': 49990,
    'Beef Liver 1kg': 52990,
    'Chocolate Pobeda 57% dark 100g': 13490,
    'Chocolate Millenium Riviera': 24990,
    'Twix 55g': 5490,
    'Millenium Milk Porous 90g': 12490
}

bought_products = {}


def new_two_lines():
    print("____________________________")
    print("")
    print("____________________________")


def validate_input_num(value):
    if value is not None and value != "":
        try:
            num = int(value)
            return 1 if num < 1 else num
        except:
            print("Incorrect input")
    print("Input cannot be empty!")


if __name__ == '__main__':
    test_user = user.User("test_user", "Test", "User", "1234567")
    users.append(test_user)
    while True:
        print("=_=_=_==_==_==_==_=> Welcome to Ecommerce Platform <=_=_=_==_==_==_==_=")
        print("1. Register")
        print("2. Buy")
        print("3. Quit")
        new_two_lines()

        menu_item = validate_input_num(input("Enter Menu number: "))

        if menu_item == 1:
            new_user = user.create()
            if new_user is None:
                print("Wrong Input")
            else:
                print("Success")
                users.append(new_user)
            new_two_lines()

        elif menu_item == 2:
            if len(users) < 2:  # you can change this to 1 if you want to continue without registering
                print("Please register to continue!")
            else:
                print()
                print("Hello, %s!" % users[len(users) - 1].firstname)
                print("Let's start shopping")
                print()
                while True:
                    for category in category_product.keys():
                        print(category)
                    print("Type 'finish' to go to checkout")
                    category_name = input("Enter Category Name:").capitalize()
                    if category_name == 'Finish':
                        break
                    elif category_name not in category_product.keys():
                        print("Category Not Found")
                    else:
                        print()
                        product_list = category_product[category_name]
                        while True:
                            for i, product in enumerate(product_list, start=1):
                                print(str(i) + ". " + product + ": " + str(product_price[product]) + " UZS")
                            print("99. Return to Category Page")
                            product_num = validate_input_num(input("Enter Product number: "))

                            if product_num == 99:
                                break
                            elif product_num > len(product_list):
                                print("Product Not Found")
                            else:
                                chosen_product = product_list[product_num - 1]

                                quantity = validate_input_num(input("Enter the quantity for %s: " % chosen_product))
                                bought_products[chosen_product] = quantity
                                new_two_lines()
                                print("So far we have:")
                                print(bought_products)
                                new_two_lines()

                sum = 0
                new_two_lines()
                for b_product in bought_products.keys():
                    b_quantity = bought_products[b_product]
                    price = product_price[b_product] * bought_products[b_product]
                    print(b_product + " x " + str(b_quantity) + " : " + str(price) + " UZS")
                    sum += price
                print("Total: " + str(sum) + " UZS")
                break

        elif menu_item == 3:
            print("See you Again!")
            new_two_lines()
            break

        else:
            print("Enter Numbers 1-3!")
            new_two_lines()
