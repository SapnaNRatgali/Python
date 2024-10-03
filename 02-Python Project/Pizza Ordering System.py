
import math  # Importing math module for rounding functions
print("This is pizza ordering system")
print('Welcome to Crust Charm Pizza')

# Taking customer name input
name = input("Enter your name: ")

# Initializing an empty list to store the customer's order
my_order = []

# Initializing a variable to store the total cost of the order
total_cost = 0

# Main ordering loop, continues until the customer chooses to exit
while True:
    # Displaying the main menu options to the customer
    print('\n1-> Veg')
    print('2-> Non-Veg')
    print('3-> Side Orders')
    print('0-> Exit')
    
    # Taking input for the main menu selection
    option = input('Please select an option: ')

    # Exiting the ordering system if the user selects '0'
    if option == '0':
        break

    # If the customer selects Veg Pizzas
    elif option == '1':  # ----------------------------------------- Veg Pizzas ----------------------------------------- #
        while True:
            # Displaying the veg pizza options
            print('\n1-> Margherita')
            print('2-> Farm House')
            print('3-> Peppy Paneer')
            print('4-> Mothers Recipe')
            print('0-> Go to Previous option')
            
            # Taking input for the veg pizza selection
            veg_option = input('Please select an option: ')

            # If the customer wants to go back to the main menu
            if veg_option == '0':
                break

            # Checking if the customer selected a valid pizza option
            if veg_option in ['1', '2', '3', '4']:
                # Asking for the pizza size (Small, Medium, Large)
                size = input('Please select size (1-> Small 2-> Medium 3-> Large): ')

                # Proceed if a valid size is selected
                if size in ['1', '2', '3']:
                    size = int(size)

                    # Handling the pricing for Margherita
                    if veg_option == '1':
                        if size == 1:
                            total_cost += 80  # Small size
                            my_order.append('Margherita (Small)')
                        elif size == 2:
                            total_cost += 190  # Medium size
                            my_order.append('Margherita (Medium)')
                        elif size == 3:
                            total_cost += 340  # Large size
                            my_order.append('Margherita (Large)')

                    # Handling the pricing for Farm House
                    elif veg_option == '2':
                        if size == 1:
                            total_cost += 135
                            my_order.append('Farm House (Small)')
                        elif size == 2:
                            total_cost += 275
                            my_order.append('Farm House (Medium)')
                        elif size == 3:
                            total_cost += 435
                            my_order.append('Farm House (Large)')

                    # Handling the pricing for Peppy Paneer
                    elif veg_option == '3':
                        if size == 1:
                            total_cost += 180
                            my_order.append('Peppy Paneer (Small)')
                        elif size == 2:
                            total_cost += 335
                            my_order.append('Peppy Paneer (Medium)')
                        elif size == 3:
                            total_cost += 500
                            my_order.append('Peppy Paneer (Large)')

                    # Handling the pricing for Mothers Recipe
                    elif veg_option == '4':
                        if size == 1:
                            total_cost += 180
                            my_order.append('Mothers Recipe (Small)')
                        elif size == 2:
                            total_cost += 335
                            my_order.append('Mothers Recipe (Medium)')
                        elif size == 3:
                            total_cost += 500
                            my_order.append('Mothers Recipe (Large)')
                else:
                    # Error message if invalid size is entered
                    print('PLEASE ENTER A VALID SIZE OPTION')
            else:
                # Error message if invalid pizza option is selected
                print('PLEASE ENTER A VALID OPTION')

    # If the customer selects Non-Veg Pizzas
    elif option == '2':  # ----------------------------------------- Non-Veg Pizzas ----------------------------------------- #
        while True:
            # Displaying the non-veg pizza options
            print('\n1-> Barbeque Chicken')
            print('2-> Chicken Fiesta')
            print('3-> Chicken Mexicana')
            print('4-> Non Veg Suprema')
            print('0-> Go to Previous option')
            
            # Taking input for the non-veg pizza selection
            nonveg_option = input('Please select an option: ')

            # If the customer wants to go back to the main menu
            if nonveg_option == '0':
                break

            # Checking if the customer selected a valid non-veg pizza option
            if nonveg_option in ['1', '2', '3', '4']:
                # Asking for the pizza size (Small, Medium, Large)
                size = input('Please select size (1-> Small 2-> Medium 3-> Large): ')

                # Proceed if a valid size is selected
                if size in ['1', '2', '3']:
                    size = int(size)

                    # Handling the pricing for Barbeque Chicken
                    if nonveg_option == '1':
                        if size == 1:
                            total_cost += 135
                            my_order.append('Barbeque Chicken (Small)')
                        elif size == 2:
                            total_cost += 275
                            my_order.append('Barbeque Chicken (Medium)')
                        elif size == 3:
                            total_cost += 435
                            my_order.append('Barbeque Chicken (Large)')

                    # Handling the pricing for Chicken Fiesta
                    elif nonveg_option == '2':
                        if size == 1:
                            total_cost += 180
                            my_order.append('Chicken Fiesta (Small)')
                        elif size == 2:
                            total_cost += 335
                            my_order.append('Chicken Fiesta (Medium)')
                        elif size == 3:
                            total_cost += 500
                            my_order.append('Chicken Fiesta (Large)')

                    # Handling the pricing for Chicken Mexicana
                    elif nonveg_option == '3':
                        if size == 1:
                            total_cost += 215
                            my_order.append('Chicken Mexicana (Small)')
                        elif size == 2:
                            total_cost += 380
                            my_order.append('Chicken Mexicana (Medium)')
                        elif size == 3:
                            total_cost += 535
                            my_order.append('Chicken Mexicana (Large)')

                    # Handling the pricing for Non-Veg Suprema
                    elif nonveg_option == '4':
                        if size == 1:
                            total_cost += 180
                            my_order.append('Non Veg Suprema (Small)')
                        elif size == 2:
                            total_cost += 335
                            my_order.append('Non Veg Suprema (Medium)')
                        elif size == 3:
                            total_cost += 500
                            my_order.append('Non Veg Suprema (Large)')
                else:
                    # Error message if invalid size is entered
                    print('PLEASE ENTER A VALID SIZE OPTION')
            else:
                # Error message if invalid pizza option is selected
                print('PLEASE ENTER A VALID OPTION')

    # If the customer selects Side Orders
    elif option == '3':  # ----------------------------------------- Side Orders ----------------------------------------- #
        while True:
            # Displaying the side order options
            print('\n1-> Calzone Pockets')
            print('2-> Chicken Wings')
            print('3-> Stuffed Garlic Bread')
            print('4-> Choco Lava Cake')
            print('0-> Go to Previous option')

            # Taking input for the side order selection
            side_option = input('Please enter your choice: ')

            # If the customer wants to go back to the main menu
            if side_option == '0':
                break

            # Handling each side order option
            if side_option == '1':
                total_cost += 85
                my_order.append('Calzone Pockets')
            elif side_option == '2':
                total_cost += 135
                my_order.append('Chicken Wings')
            elif side_option == '3':
                total_cost += 110
                my_order.append('Stuffed Garlic Bread')
            elif side_option == '4':
                total_cost += 70
                my_order.append('Choco Lava Cake')
            else:
                # Error message if an invalid side order option is selected
                print('PLEASE ENTER A VALID OPTION')

    # Error message if the customer enters an invalid main menu option
    else:
        print('PLEASE ENTER A VALID OPTION')

# After the ordering process is complete, calculate the final amount
print()
print(f"Thank you {name} for ordering....")

# Calculating 5% GST on the total cost
gst = math.ceil(total_cost * 0.05)

# Displaying the customer's final order and costs
print('\nYour Final Order is:', my_order)
print('Basic Cost:', total_cost)
print('GST:', gst)
print('Amount Payable:', total_cost + gst)
