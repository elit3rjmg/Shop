# author: RJ
# Shop v1.1

itemsAvailList = {
    'sugar' : 50,
    'salt' : 40,
    'milk' : 25,
    'coffee' : 60
} 

itemsAvail = ['sugar', 'salt', 'milk', 'coffee']
print(itemsAvail)

applyDiscount = 15
cashInHand = 250
totalPrice = 0

shopCart = []
while len(itemsAvail) > 0:
    shop = input('What would you like to buy?: ').lower()
    if shop in itemsAvail:
        shopCart.append(shop)
        totalPrice += itemsAvailList[shop]
    else:
        print('Item not available')
        continue

    ask = input('Would you like to continue shopping? (Y/N): ').lower()
    if ask == 'n':
        price = totalPrice
        break
    elif ask == 'y':
        continue
    else:
        print('Invalid Input.....')
        break

print(shopCart)
disVal = (applyDiscount/100) * totalPrice
totalPay = totalPrice - disVal

print('Total Price: Rs.'+str(totalPrice))
print('Discount:', str(applyDiscount) + '%')
print('Total Price after Discount: Rs.'+str(totalPay))
if cashInHand <= totalPay:
    print("sorry you don't have enough money to purchase these items")
    exit  
else:
    print('Thank you for shopping!')