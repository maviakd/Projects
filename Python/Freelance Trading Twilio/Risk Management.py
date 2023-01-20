def buy(order_type):
    def test(x, y, risk):
        while (x + y != risk):
            x+=1
            if (x+y == risk):
                break
            y += 1
        if (x == y):
            x = x-1
            y = y+1
        return y, x

    while True:
        try:
            balance = int(input("Enter account balance\t"))
            break
        except:
            print("Whole numbers whithout symbols")

    while True:
        try:
            risk = int(input("Enter your risk percentage\t"))
            break
        except:
            print("Whole numbers only without the percentage/modulus sign")
    x, y = 0, 0
    lot = float(input("Enter lot size (.01, 1, 1.1...)\t"))

    price = str(input("Enter Market Price\t"))
    try:
        price = int(price)
    except ValueError:
        price = float(price) * 100
        price = int(price)

    percentages = test(x, y, risk)
    print(f"return percentages are {percentages[0]} {percentages[1]}")
    pips = risk/lot
    risk_amount = (balance*risk)/100
    sl1 = percentages[1]/lot
    sl2 = percentages[0]/lot

    if order_type == "buy":
        price_action1 = (price-sl1) / 100
        price_action2 = (price-sl2) / 100
        tp1 = (price + (sl1*3)) / 100
        tp2 = (price + (sl2*3)) / 100
    else:
        price_action1 = (price + sl1) / 100
        price_action2 = (price + sl2) / 100
        tp1 = (price - (sl1*3)) / 100
        tp2 = (price - (sl2*3)) / 100

    print(f"Marker price @ {price}")
    print("This system uses a 1/3 W/L Ratio")
    print(f"You are risking a loss of ${risk_amount} ")
    print(f"With that lot size you can loose up to {pips} pips")
    print(f"SL ONE is {sl1} pips away from price which will be {price_action1}")
    print(f"SL TWO is {sl2} pips away from price which will be {price_action2}")
    print(f"Both SL together accumilate to {sl1 + sl2} pips which is ${(sl1 + sl2)} with a {lot} lot\n")
    print("######################")
    print(f"TP ONE is {tp1}")
    print(f"SL ONE is {price_action1}")
    print(f"TP TWO is {tp2}")
    print(f"SL TWO is {price_action2}")
    print("#######################")

    while True:
        again = input("Would you like to try again (Yes/No)(Y/N)?")
        if again.lower() == "yes" or again.lower() == "y":
            return True
        if again.lower() == "no" or again.lower() == "n":
            return False
        print("Wring Input")


again = True
while True:
    again = True	
    order_type = str(input("Is it a buy or a sell?\t"))
    if order_type.lower() == "buy":
        again = buy(order_type)
    elif order_type.lower() == "sell":
        again = buy(order_type)
    else:
        print("Wrong input")
    print(f"AGAIN came back as {again}")
    if again == False:
        input("Terminated. Press enter to exit...")
        break

