totpizzanum = 0
totpastanum = 0

totpizzaamt = 0
totpastaamt = 0

totamount = 0


while True:
    
    print("---- MENU ----")
    print("1. PIZZA")
    print("2. PASTA")
    print("3. PIZZA AND PASTA")
    print("4. EXIT")
    
    ch = int(input("Enter your choice : "))
    
    if ch == 1 :
        numpizza = int(input("Enter the number of pizzas : "))
        numgarlicbread = 0
        if numpizza == 1:
            pizzacost = 12
        elif numpizza == 2:
            pizzacost = 22
        elif numpizza >= 3:
            pizzacost = numpizza * 10
            numgarlicbread = numpizza // 3
        
        totpizzanum = totpizzanum + numpizza
        totpizzaamt = totpizzaamt + pizzacost
 
        print(" Total amount to pay : ", pizzacost)
        print("No. of garlic bread free : ", numgarlicbread )
        print()
    
    elif ch == 2:
        
        numpasta = int(input("Enter the number of pastas : "))
        
        numcolddrinks = 0
        
        if numpasta == 1:
            pastacost = 8
        elif numpasta == 2:
            pastacost = 15
        elif numpasta >= 3:
            pastacost = numpasta * 7
            numcolddrinks = numpasta // 3
        
        totpastanum = totpastanum + numpasta
        totpastaamt = totpastaamt + pastacost
        
        print("Total amount to pay : ", pastacost)
        print("Total number of cold drinks free : ",numcolddrinks)
        print()
    elif ch == 3 :
        numpizza = int(input("Enter the number of pizzas : "))
        numgarlicbread = 0
        numbaklava = 0
        if numpizza == 1:
            pizzacost = 12
        elif numpizza == 2:
            pizzacost = 22
        elif numpizza >= 3:
            pizzacost = numpizza * 10
            numgarlicbread = numpizza // 3
        
        totpizzanum = totpizzanum + numpizza
        totpizzaamt = totpizzaamt + pizzacost
        
        numpasta = int(input("Enter the number of pastas : "))
        
        numcolddrinks = 0
        
        if numpasta == 1:
            pastacost = 8
        elif numpasta == 2:
            pastacost = 15
        elif numpasta >= 3:
            pastacost = numpasta * 7
            numcolddrinks = numpasta // 3
        
        payamt  = pizzacost + pastacost
        
        totpastanum = totpastanum + numpasta
        totpastaamt = totpastaamt + pastacost
        
        if numpizza >=3 and numpasta >= 3:           
            numbaklava = ((numpizza//3) + (numpasta)//3) // 3
        
        print("Total amount to pay : ", payamt)
        print("No. of garlic bread free : ", numgarlicbread )
        print("Total number of cold drinks free : ",numcolddrinks)
        print("No. of baklava free : ", numbaklava)
        print()
    
    elif ch == 4:
        break

    else:
        print("Wrong choice !!!")
        print()

totamount = totpastaamt + totpizzaamt

print("--- DAY SUMMARY REPORT ---")
print()

print("NUM OF PIZZAS SOLD : ", totpizzanum)
print("AMOUNT EARNED FROM PIZZA SALE : ", totpizzaamt)
print("NUM OF PASTAS SOLD : ", totpastanum)
print("AMOUNT EARNED FROM PASTA SALE : ", totpastaamt)

print()
print("TOTAL MONEY EARNED IN THE DAY : ", totamount)