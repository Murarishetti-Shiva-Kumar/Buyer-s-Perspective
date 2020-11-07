print("\n" * 1)

import datetime  # Deltatime library, to get Real Date information.
import os

list_freelancers = []  # Variable List of Freelancers
list_customer_payment = []  # Variable List of Customers and payment status
list_events = []    # Variable List of Events

list_package_price = [0] * 100

navigator_symbol = "/"
if os.name == "nt":
    navigator_symbol = "\\"  # This will make the program runnable on Windows


def def_default():
    global list_customer_payment, list_freelancers, list_events, list_package_ordered, list_package_price
    list_package_ordered = [0] * 100  # Create a list, length 100. Max index number is 99.
    def_default()


def def_main():
    while True:  # Repeat Menu until stops.
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"  # Design for Main Menu.
                                                  "\t(O) ORDER FOR EVENT SCHEDULE\n" 
                                                  "\t(R) REPORT\n"
                                                  "\t(P) PAYMENT\n"
                                                  "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input(
            "Please Select Your Operation: ")).upper()  # Input, have to choose operation. Make everything UPPER symbol with "". Eg Options: "O" or "R" or "P" or "E"
        if (len(input_1) == 1):
            if (input_1 == "O"):
                print("\n" * 4)
                def_order_menu()
                break
            elif (input_1 == "R"):
                print("\n" * 4)
                def_report()
                break
            elif (input_1 == "P"):
                print("\n" * 4)
                def_payment()
                break
            elif (input_1 == "E"):
                print("*" * 32 + "THANK YOU. SEE YOU AGAIN!!" + "*" * 31 + "\n")  # Good bye comment.
                break  # Stop repeating Main Menu.
            else:  # If O, R, P, E not inserted then...
                print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.
        else:  # If input length not equal to 1...
            print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def def_order_menu():
    while True:  # While looping to keep menu alive
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"  # Main Menu
              "\t(F) FREELANCERS AND PACKAGES\n"
              "\t(A) ACTIVE EVENTS\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()  # Options  : "F" or "A" or "M" or "E".
        if len(input_1) == 1:
            if (input_1 == "F"):  # Easy Access Checking Logic
                print("\n" * 4)
                def_freelancer_package_order()  # Show Freelancers/Packages Menu
                break
            elif (input_1 == "A"):
                print("\n" * 4)
                def_active_events()  # Show Events Menu
                break
            elif (input_1 == "M"):
                print("\n" * 4)
                def_main()  # Show Main Menu
                break
            elif (input_1 == "E"):
                print("*" * 32 + "THANK YOU. SEE YOU AGAIN!!" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Invalid input.
        else:
            print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")    # Invalid input.


def def_full_file_reader():
    file_freelancers = open('/Users/aditya/PycharmProjects/pythonProject/hackathon2020' + navigator_symbol + 'list_freelancers.fsd',
                      'r')  # Reading Freelancers List
    for i in file_freelancers:
        list_freelancers.append(str(
            i.strip()))
    file_freelancers.close()

    file_payment = open('/Users/aditya/PycharmProjects/pythonProject/hackathon2020' + navigator_symbol + 'list_customer_payment.fsd',
                       'r')  # Reading Packages List
    for i in file_payment:
        list_customer_payment.append(str(i.strip()))
    file_payment.close()

    file_events = open('/Users/aditya/PycharmProjects/pythonProject/hackathon2020' + navigator_symbol + 'list_events.fsd',
                         'r')  # Reading Events List
    for i in file_events:
        list_events.append(str(i.strip()))
    file_events.close()

    i = 0
    while i <= (len(list_freelancers) - 1):
        if 'ACTIVE' in list_freelancers[i]:
            list_freelancers[i] = str(list_freelancers[i][:list_freelancers[i].index('ACTIVE') - 1]) + ' ' * (
                        20 - (list_freelancers[i].index('ACTIVE') - 1)) + str(list_freelancers[i][list_freelancers[i].index('ACTIVE'):])
        i += 1

    i = 0
    while i <= (len(list_customer_payment) - 1):
        if 'ACTIVE' in list_customer_payment[i]:
            list_customer_payment[i] = str(list_customer_payment[i][:list_customer_payment[i].index('ACTIVE') - 1]) + ' ' * (
                        20 - (list_customer_payment[i].index('ACTIVE') - 1)) + str(list_customer_payment[i][list_customer_payment[i].index('ACTIVE'):])
        i += 1

    i = 0
    while i <= (len(list_events) - 1):
        if 'ACTIVE' in list_events[i]:
            list_events[i] = str(list_events[i][:list_events[i].index('ACTIVE') - 1]) + ' ' * (
                        20 - (list_events[i].index('ACTIVE') - 1)) + str(list_events[i][list_events[i].index('ACTIVE'):])
        i += 1


def_full_file_reader()


def def_file_sorter():
    global list_freelancers, list_customer_payment, list_events
    list_freelancers = sorted(list_freelancers)
    list_customer_payment = sorted(list_customer_payment)
    list_events = sorted(list_events)

    i = 0
    while i < len(list_freelancers):
        #        list_package_price[i] = float(list_freelancers[i][int(list_freelancers[i].index("ACTIVE") + 3):])
        list_package_price[i] = 100
        i += 1

    i = 0
    while i < len(list_customer_payment):
        #       list_package_price[40 + i] = float(list_customer_payment[i][int(list_customer_payment[i].index("ACTIVE") + 3):])
        list_package_price[i] = 200
        i += 1

    i = 0
    while i < len(list_events):
        #        list_package_price[80 + i] = float(list_events[i][int(list_events[i].index("ACTIVE") + 3):])
        list_package_price[i] = 300
        i += 1


def_file_sorter()

def def_freelancer_package_order():
    while True:
        print("*" * 29 + "AVAILABLE FREELANCERS" + "*" * 29)
        print("|NO| |FREELANCER NAME|       |SPECIALIST|                                |PRICE|")  # Freelancers Menu Structure

        i = 0
        while i < len(list_freelancers):
            print(" (" + str(1 + i) + ")" + " " + str(list_freelancers[i]))
            i += 1
            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)
            input_1 = input("Please Select Freelancer for your planned event: ").upper()
            if (input_1 == "M"):
                print("\n" * 4)
            def_main()  # Navigate Back to main menu
            break
        if (input_1 == "E"):
            print("*" * 32 + "THANK YOU. SEE YOU AGAIN!!" + "*" * 31 + "\n")
            break
        if (input_1 == "P"):
            print("\n" * 4)
            def_report()  # navigate to payment
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 4)
                print("Successfully Ordered: " + str(list_events[int(input_1) - 81]))
                list_package_ordered[int(input_1) - 1] = 1
                def_active_events()
                break
            else:
                print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_active_events():
    while True:
        print("*" * 29 + "AVAILABLE EVENTS" + "*" * 29)
        print("|NO| |EVENT NAME|           |PRICE|")  # Events Menu Structure

        i = 0
        while i < len(list_events):
            print(" (" + str(1 + i) + ")" + " " + str(list_events[i]))
            i += 1
            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)
            input_1 = input("Please Select Your Operation: ").upper()
            if (input_1 == "M"):
                print("\n" * 4)
            def_main()  # Navigate Back to main menu
            break
        if (input_1 == "E"):
            print("*" * 32 + "THANK YOU. SEE YOU AGAIN!!" + "*" * 31 + "\n")
            break
        if (input_1 == "P"):
            print("\n" * 4)
            def_payment()  # navigate to payment report
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 4)
                print("Successfully Ordered: " + str(list_events[int(input_1) - 81]))
                list_package_ordered[int(input_1) - 1] = 1
                def_active_events()
                break
            else:
                print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment():
    while True:
        print("*" * 29 + "CURRENT ORDERS" + "*" * 41)
        print("|NO| |CUSTOMER NAME|        |EVENT SELECTION|       |AMOUNT PAID|       |AMOUNT DUE|")  # Payment Menu Structure

        i = 0
        while i < len(list_customer_payment):
            print(" (" + str(1 + i) + ")" + " " + str(list_customer_payment[i]))
            i += 1
            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)
            input_1 = input("Please Select Your Operation: ").upper()
            if (input_1 == "M"):
                print("\n" * 4)
            def_main()  # Navigate Back to main menu
            break
        if (input_1 == "E"):
            print("*" * 32 + "THANK YOU. SEE YOU AGAIN!!" + "*" * 31 + "\n")
            break
        if (input_1 == "P"):
            print("\n" * 4)
            def_report()  # navigate to payment
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 4)
                print("Successfully Ordered: " + str(list_events[int(input_1) - 81]))
                list_package_ordered[int(input_1) - 1] = 1
                def_active_events()
                break
            else:
                print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_report():
    while True:
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        file_report = open('/Users/aditya/PycharmProjects/pythonProject/hackathon2020' + navigator_symbol + 'report.fsd', 'r').read()  # Reading out reports from report.fsd
        print(file_report)
        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == "M"):
            print("\n" * 4)
            def_main()  # Navigate back to menu
            break
        elif (input_1 == "E"):
            print("*" * 32 + "THANK YOU. SEE YOU AGAIN!!" + "*" * 31 + "\n")  # Exit and break up the loop
            break
        else:
            print("\n" * 4 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def_main()  # Execute Main menu Loop
