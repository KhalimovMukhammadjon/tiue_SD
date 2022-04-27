import main


class User:
    def __init__(self, username, firstname, lastname, phone_number):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number


def create():
    username = input("Enter Username: ")

    if username is None or username == "":
        return None
    for user in main.users:
        if user.username == username:
            print("This Username Already Exists")
            return None

    firstname = input("Enter Firstname: ")

    if firstname is None or firstname == "" and not firstname.isalpha():
        return None

    lastname = input("Enter Lastname: ")

    if lastname is None or lastname == "" and not lastname.isalpha():
        return None

    phone = input("Enter Phone Number: ")

    if phone is None or phone == "":
        return None
    new_user = User(username, firstname, lastname, phone)
    return new_user
