print('In this program we will calculete a restaurant bill')
print(""" Here is the menu items of restaurant 
        1. Pizza 90rs per piece
        2. Soup 30rs per serve
        3. Dring 20 rs per serve
""")
menuList = ['Pizza', 'Soup', 'Drink']
priceList = [90, 30, 20]
numberOfTakenItemList = [0,0,0]
while 1>0:
    print('Enter the number to select menu')
    item = int(input())
    print(f"Enter how many {menuList[item-1]}s taken by customer")
    numberOfTakenItem = int(input())
    print(f'Price of {numberOfTakenItem} {menuList[item-1]} is calculeted as {numberOfTakenItem * priceList[item-1]}')
    numberOfTakenItemList[item-1] += int(numberOfTakenItem)
    print('To continue press "y" to break press "n"')
    userChoice = str(input())
    if userChoice == 'y':
        continue
    else:
        break

print("Final bill is as follows")
totalPrice = 0
for index, numberOfTakenItem in enumerate(numberOfTakenItemList):
    if numberOfTakenItem != 0:
        cost = numberOfTakenItem*priceList[index]
        print(f'Number of {menuList[index]} taken:: {numberOfTakenItem} cost {cost}' )
        totalPrice += cost
else:
        print(f"Total bill is {totalPrice} rupees")