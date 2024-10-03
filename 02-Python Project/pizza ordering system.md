
# This Python code is a Pizza Ordering System for "Crust Charm Pizza." 
- The system allows a customer to choose and order pizzas (both veg and non-veg) as well as side orders. 
- This would be classified as a basic to medium-level Python project. 

Here's a breakdown of how the code works:

1. Initialization:
- The code starts by greeting the customer and taking their name as input.
- An empty list (my_order) is used to store the customer's chosen items.
- The variable total_cost is initialized to 0 to keep track of the total cost of the order.

2. Main Menu:
- A while loop presents the main menu with three categories:
    - Veg Pizzas
    - Non-Veg Pizzas
    - Side Orders
    - An option to Exit the ordering process.

3. Veg Pizzas Menu:
- If the customer selects the "Veg" category, they are presented with 4 pizza options:
    - Margherita
    - Farm House
    - Peppy Paneer
    - Mothers Recipe
- The customer can select one of these pizzas and then choose the size (Small, Medium, Large).
- Depending on the selection, the system adds the pizza to the order and updates the total cost with the respective price.

4. Non-Veg Pizzas Menu:
- If the customer selects "Non-Veg," they are presented with 4 non-veg pizza options:
    - Barbeque Chicken
    - Chicken Fiesta
    - Chicken Mexicana
    - Non-Veg Suprema
- Like the veg pizza menu, the customer can select the pizza and choose the size, and the system will add the pizza to the order and update the total cost.

5. Side Orders Menu:
- In this menu, the customer can add side orders such as:
     - Calzone Pockets
     - Chicken Wings
     - Stuffed Garlic Bread
     - Choco Lava Cake
- Each side item has a fixed cost, which is added to the total.

6. Exiting and Finalizing Order:
- The customer can exit the order at any time by selecting "0" from the menus.
- Once they exit, the system:
- Displays the customer's final order (my_order list).
- Displays the basic cost of the order.
- Calculates a 5% GST on the total cost and adds it to display the final amount payable.

7. Mathematical Calculations:
- GST is calculated as 5% of the total cost, rounded up using math.ceil().

8. Print Statements:
- At the end, the system thanks the customer, shows the items they ordered, the basic cost, the calculated GST, and the total amount they need to pay.


# Example Flow:
- A customer named "Priya" selects a Margherita Pizza (Medium) and Chicken Wings.
- The system adds the price of both items to the total cost.
- The system calculates GST on the total and then displays the amount payable.





