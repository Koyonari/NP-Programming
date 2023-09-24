# Menu options
menu = '-------------------\n1. Add Order\n2. Summarize Orders\n3. Quit\n-------------------'
# Price list for items
prices = {'chicken' : 8.50,
          'steak' : 13.80,
          'fish' : 9.80,
          'pasta' : 9.50,
          'coffee' : 2.50,
          'tea' : 1.80,
          'water' : 0.50}

# List to store orders
summary_orders = []

# Function to add order
def add_order():
  print('Item', ' ' * 6, 'Price')
  print('----', ' ' * 6, '-----')
  # Print items and their prices from prices dictionary
  for item, price in prices.items():
    print(f'{item.capitalize()}', ' ' * (10 - len(item)), f'${price:.2f}')
  # Get user input for item and sets
  item = input('Your order? ').lower()
  if item in prices.keys():
    sets = int(input('Enter sets: '))
    # Calculate total price of items
    total_price = prices[item] * sets
    order = {'item': item, 'sets': sets, 'total_price': total_price}
    summary_orders.append(order)
    print(f'\n{sets} set(s) of {item.capitalize()} ordered.')
  else:
    print(item, 'is not available.')

# Function to summarize orders
def summarize_orders():
  print('Item', ' ' * 6, 'Quantity')
  print('----', ' ' * 6, '--------')
  total_price = 0
  # Print orders
  for order in summary_orders:
    print(f'{order["item"].capitalize()}', ' ' * (10 - len(order['item'])), f'{order["sets"]}')
    total_price += order['total_price']
  # Print total price of all orders
  print(f'Total cost = ${total_price:.2f}')

# Main code block
while True:
  # Show menu options
  print(menu)
  user_choice = input('Your choice? ')
  if user_choice == '1':
    add_order()
  elif user_choice == '2':
    summarize_orders()
  elif user_choice == '3':
    print('\nThank you for visiting. Goodbye!')
    break
  else:
    print('\nInvalid input. Please input a number from 1 to 3.')
