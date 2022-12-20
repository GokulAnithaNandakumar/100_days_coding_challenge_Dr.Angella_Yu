MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water=resources['water']
milk=resources['milk']
coffee=resources['coffee']
money=0
list=["off","report","espresso","latte","cappuccino"]
while True:
    ing=True
    z=input("What would you like? (espresso/latte/cappuccino):")
    c=z.lower()
    if c not in list:
        print("Enter a valid product.")
        ing=False
    if c=="off":
       print("Thank you for shopping!")
       break
    if c.lower()=="report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    else:
        for b in MENU:
            if b==c:
                for d in MENU[c]['ingredients']:
                    if int(MENU[c]['ingredients'][d])>int(resources[d]):
                        print(f"Sorry there is not enough {d}.")
                        ing=False
                        break

        if ing:
            q = int(input("Insert the number of quarters: "))
            d = int(input("Insert the number of dimes: "))
            n = int(input("Insert the number of nickels: "))
            p = int(input("Insert the number of pennies: "))
            l=[float(q*0.25),float(p*0.01),float(n*0.05),float(d*0.1)]
            cos=round(sum(l), 2)
            print(cos)
            for l in MENU:
                if l==c:
                    co=str(MENU[l]['cost'])
                    cor=float(co)
                    if cos<cor:
                        print("Sorry that's not enough money. Money refunded.")
                    elif cos>=cor:
                        r=cos-cor
                        money+=cor

                        if r!=0:
                            print(f"Here is ${r} dollars in change.")

                        if l==c:
                            a=MENU[l]['ingredients']['water']
                            q=int(a)
                            b=MENU[l]['ingredients']['coffee']
                            r=int(b)
                            y=MENU[l]['ingredients']['milk']
                            s=int(y)
                            resources['water']-=q
                            resources['coffee']-=r
                            resources['milk']-=s
                            print(f"Here is your {c}. Enjoy!")
