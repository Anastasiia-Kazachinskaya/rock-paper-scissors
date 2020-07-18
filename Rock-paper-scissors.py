import random

name = input("Enter your name: ")
print("Hello, ", name)

user_option = input()
a = 0

def user_rating():
    if user_option == '!rating':
        if name:
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(a))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()

while user_option:

    list_of_options = ["rock", "paper", "scissors"]

    if user_option != list_of_options[1] and user_option != list_of_options[0] and user_option != list_of_options[
        2] and user_option != "!exit" and user_option != "!rating":
        print("Invalid input")
        user_option = input()
    if user_option == "!exit":
        print("Bye!")
        break

    computer_choice = random.choice(list_of_options)

    if user_option == list_of_options[0]:
        if computer_choice == list_of_options[1]:
            print("Sorry, but computer chose {0}".format(list_of_options[1]))
            user_option = input()
        elif computer_choice == list_of_options[0]:
            print("There is a draw ({0})".format(list_of_options[0]))
            a += 50
            user_option = input()
        else:
            print("Well done. Computer chose {0} and failed".format(list_of_options[2]))
            a += 100
            user_option = input()
    elif user_option == list_of_options[1]:
        if computer_choice == list_of_options[2]:
            print("Sorry, but computer chose {0}".format(list_of_options[2]))
            user_option = input()
        elif computer_choice == list_of_options[0]:
            print("Well done. Computer chose {0} and failed".format(list_of_options[0]))
            a += 100
            user_option = input()
        else:
            print("There is a draw ({0})".format(list_of_options[1]))
            a += 50
            user_option = input()

    elif user_option == list_of_options[2]:
        if computer_choice == list_of_options[0]:
            print("Sorry, but computer chose {0}".format(list_of_options[0]))
            user_option = input()
        elif computer_choice == list_of_options[1]:
            print("Well done. Computer chose {0} and failed".format(list_of_options[1]))
            a += 100
            user_option = input()
        else:
            print("There is a draw ({0})".format(list_of_options[2]))
            a += 50
            user_option = input()
    if user_option == "!rating":
        user_rating()
        user_option = input()