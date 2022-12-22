# author: RJ
# Shop v1.2

class receipt:

    def discount(applyDiscount, totalPrice):
        disVal = (applyDiscount/100) * totalPrice
        totalPrice -= disVal
        return float(totalPrice)
    
    def counter(totalPay):
        print('\nDiscount:', str(applyDiscount) + '%')
        print('Total Price after Discount: Rs.'+str(totalPay))
        print('Thank you for shopping!')

itemsAvailList = {
    'milk' : 25,
    'salt' : 40,
    'sugar' : 50,
    'coffee' : 60,
    'canned tuna' : 90,
    'protein shake' : 120    
} 

items = list(itemsAvailList.keys())
print(items)

applyDiscount = 15
cashInHand = 250
totalPrice = 0

shopCart = []
while len(itemsAvailList) > 0:
    
    shop = input('\nWhat would you like to buy?: ').lower()
    if shop in itemsAvailList:
        shopCart.append(shop)
        totalPrice += itemsAvailList[shop]
        
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

while cashInHand <= totalPrice:
    print('Total: Rs.' + str(totalPrice))
    print("Sorry, you don't have enough money to purchase these items.")
    
    ask = input('Would you like to remove some items? (Y/N): ').lower()   
    if ask == 'n':
        print('Please shop again next time!')
        break

    elif ask == 'y':
        ask = input('Which item would like to remove?: \n')
        shopCart.remove(ask)
        totalPrice -= itemsAvailList[ask]              
        totalPay = totalPrice
        
        print(shopCart)   
        print('Total price now: Rs.' + str(totalPrice))

        if cashInHand <= totalPay:
            continue
        
        else:
            break

totalPay = receipt.discount(applyDiscount, totalPrice)    
receipt.counter(totalPay)