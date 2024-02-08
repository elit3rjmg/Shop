# author: RJ
# Shop v2.1

import pandas as pd
from tabulate import tabulate as table

class receipt:

    def discount(applyDiscount, totalPrice):
        disVal = (applyDiscount/100) * totalPrice
        totalPrice -= disVal
        return float(totalPrice)
    
    def counter(totalPay):
        print('\nDiscount:', str(applyDiscount) + '%')
        print('Total Price after Discount: Rs.'+str(totalPay))
        print('Thank you for shopping!')

#    def debugMenu():
#       print("Debug menu:\n")

itemData = [
        {'Item' : 'milk', 'Quantity' : 32, 'Price' : 25},
        {'Item' : 'salt', 'Quantity' : 22, 'Price' : 40},
        {'Item' : 'sugar', 'Quantity' : 44, 'Price' : 50},
        {'Item' : 'coffee', 'Quantity' : 28, 'Price' : 60},
        {'Item' : 'canned tuna', 'Quantity' : 16, 'Price' : 90},
        {'Item' : 'protein shake', 'Quantity' : 12, 'Price' : 120 },
        {'Item' : 'choco bar', 'Quantity' : 54, 'Price' : 45 },
        {'Item' : 'honey syrup', 'Quantity' : 35, 'Price' : 65 },
        {'Item' : 'potato chips', 'Quantity' : 50, 'Price' : 20},]

itemData2 = [
        {'Item' : 'Pencil', 'Quantity' : 120, 'Price' : 5},
        {'Item' : 'eraser', 'Quantity' : 90, 'Price' : 2},
        {'Item' : 'ball pen', 'Quantity' : 60, 'Price' : 20},
        {'Item' : 'ruler', 'Quantity' : 65, 'Price' : 3},
        {'Item' : 'notebook', 'Quantity' : 16, 'Price' : 90},
        {'Item' : 'geometry box', 'Quantity' : 55, 'Price' : 75 }]

itemsPrice = {
    'milk' : 25,
    'salt' : 40,
    'sugar' : 50,
    'coffee' : 60,
    'canned tuna' : 90,
    'protein shake' : 120,
    'choco bar' : 45,
    'honey syrup' : 65,
    'potato chips' : 20,
    'pencil' : 5,
    'eraser' : 2,
    'ball pen' : 10,
    'ruler' : 3,
    'notebook' : 15,
    'geometry box' : 75,
} 

itemFrame = pd.DataFrame(itemData, index=[1,2,3,4,5,6,7,8,9])
itemFrame2 = pd.DataFrame(itemData2, index=[1,2,3,4,5,6])

enter = int(input("Enter Balance: "))
cashInHand = enter
cash = cashInHand

applyDiscount = 15
totalPrice = 0

shopCart = []
while len(itemsPrice) > 0:
    
    print(table(itemFrame, headers='keys', tablefmt='psql'))
    print(table(itemFrame2, headers='keys', tablefmt='psql'))
    print("Balance: Rs."+str(cash))

    shop = input('\nWhat would you like to buy?: ').lower()
    if shop in itemsPrice:
        shopCart.append(shop)
        totalPrice += itemsPrice[shop]
        cash -= itemsPrice[shop]

        print('Cart:',shopCart)
        print('Total Price: Rs.'+str(totalPrice))

    else:
        print('Item not available')
        continue

    ask = input('\nWould you like to continue shopping? (Y/N): ').lower()
    if ask == 'n':
        break
    
    elif ask == 'y':
        continue

    else:
        print('Invalid Input.....')
        continue

else:
    print('The store is closed at the moment')
    exit()

while cashInHand < totalPrice:
    print('Total: Rs.' + str(totalPrice))
    print("Sorry, you don't have enough money to purchase these items.")
    
    ask = input('Would you like to remove some items? (Y/N): ').lower()   
    if ask == 'n':
        print('Please shop again next time!')
        break

    elif ask == 'y':
        ask = input('Which item would like to remove?: \n')
       
        shopCart.remove(ask)
        totalPrice -= itemsPrice[ask]              
        totalPay = totalPrice
        cash += itemsPrice[ask]

        print(shopCart)   
        print('Total price now: Rs.' + str(totalPrice)) 

        if cashInHand < totalPay:
            continue
        
    else:
        break

totalPay = receipt.discount(applyDiscount, totalPrice)    
receipt.counter(totalPay)