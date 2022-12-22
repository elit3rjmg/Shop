#price:
sugar = 50
salt = 40
milk = 25
coffee = 60

itemsAvail = ['sugar', 'salt', 'milk', 'coffee']
print(itemsAvail)

applyDiscount = 15
cashInHand = 250
totalPrice = 0

shopCart = []
while len(itemsAvail) > 0:
    shop = input('What would you like to buy?: ').lower()
    if shop in itemsAvail:
        if shop == 'sugar':
            totalPrice += sugar
            shopCart.append('sugar')
        elif shop == 'salt':
            totalPrice += salt
            shopCart.append('salt')
        elif shop == 'milk':
            totalPrice += milk
            shopCart.append('milk')
        elif shop == 'coffee':
            totalPrice += coffee
            shopCart.append('coffee')
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