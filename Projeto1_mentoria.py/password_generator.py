import random


def password_generator():

    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowcase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbols = ['!', '?', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}']

    print("Welcome!! Let´s start to create a new password.\n")

    number_of_characters = int(input("How many character should there be? Your password must contain a minimum of 4 "
                                     "and a maximum of 10 characters: \n"))
    if (number_of_characters < 4 or number_of_characters > 10):
        print("Your password must contain a minimun of 4 and maximun of 10 characters.\n")
        number_of_characters = int(
            input("How many character should there be? Your password must contain a minimum of 4 "
                  "and a maximum of 10 characters: \n"))

    pass_letters = str(input("Should it have uppercase letters? Answer Y or N\n").strip().upper())
    pass_numbers = str(input("Should it include numbers and special characters? Answer Y or N\n").strip().upper())
    pass_simbols = str(input("Should it have simbols? Answer Y or N\n").strip().upper())

    if pass_letters == "Y" and pass_numbers == "Y" and pass_simbols == "Y":
        password_all = (uppercase_letters + lowcase_letters + numbers + simbols)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "N" and pass_numbers == "Y" and pass_simbols == "Y":
        password_all = (lowcase_letters + numbers + simbols)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "N" and pass_numbers == "N" and pass_simbols == "Y":
        password_all = (lowcase_letters + simbols)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "N" and pass_numbers == "N" and pass_simbols == "N":
        password_all = (lowcase_letters)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "Y" and pass_numbers == "Y" and pass_simbols == "N":
        password_all = (lowcase_letters + uppercase_letters + numbers)
        password = password_list(password_all, number_of_characters)

    elif pass_letters == "Y" and pass_numbers == "N" and pass_simbols == "N":
        password_all = (lowcase_letters + uppercase_letters)
        password = password_list(password_all, number_of_characters)

    print('Your new password is: ' + password)


def password_list(password_all, number_of_characters):
    password = "".join(random.sample(password_all, number_of_characters))
    return password


if __name__ == "__main__":
    password_generator()
