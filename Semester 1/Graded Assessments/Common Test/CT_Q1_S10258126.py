#An Yong Shyan (S10258126B) - IT03

require_var = input('Do you require toppings? [Yes / No]: ')
toppings_set_var = int(input('Portions of toppings required: '))
loyalty_var = input("Do you have the 'loyalty' card? [Yes / No]: ")
total_cost = 2.5
if require_var == "Yes":
    total_cost = toppings_set_var * 1.2 + total_cost
if loyalty_var == "Yes":
    total_cost = 0.9 * total_cost
print("Total cost: ${:.2f}".format(total_cost))
