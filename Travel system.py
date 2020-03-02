departure = ["Auckland", "Wellington", "Christchurch"]
destinations = ["Sydney", "Tonga", "Shanghai", "London"]


def display(a):
    length = len(a)
    for n in range (0,length):
        print(n+1, a[n])
        
          

flight_cost = 0
accomodation_cost = 0


ask = True

while ask == True:

    menu = True
    
    while menu == True:
        
        display(departure)
        print("")
        
        depart = input("Enter a number for location that you are departuring: ")
        print("")
        print("")

        if depart == "1":
            menu = False
        
        elif depart == "2":
            flight_cost = 100
            menu = False
        
        elif depart == "3":
            flight_cost = 150
            menu = False
            
        else:
            print("Enter a number between 1 to 3")
            print("")
            print("")
    
    
    
    menu = True
            
    while menu == True:
        display(destinations)
        print("")
                
        destination = input("Enter a number for location that you want to go: ")
        print("")
        print("")
        if destination == "1":
            flight_cost = flight_cost + 326
            menu = False
                    
        elif destination == "2":
            flight_cost = flight_cost + 378
            menu = False
                    
        elif destination == "3":
            flight_cost = flight_cost + 1436
            menu = False
                    
        elif destination == "4":
            flight_cost = flight_cost + 2376
            menu = False
                    
        else:
            print("Enter a number between 1 to 4")
            print("")
            print("")
        
    menu = True

    while menu == True:
        integer = True
        while integer == True:
            try:
                stay = int(input("Enter a number of nights you are staying: "))
                        
                integer = False
                        
            except ValueError:
                print("Enter an integer")
                        
            print("")
            print("")
        if stay == 0:
            print("You should be staying at least one night")
        
        else:
            if destination == "1":
                accomodation_cost = 120 * stay
                    
            elif destination == "2":
                accomodation_cost = 40 * stay
                    
            elif destination == "3":
                accomodation_cost = 60 * stay
                    
            else:
                accomodation_cost = 80 * stay
                
            menu = False
                
        if stay >= 3:
            accomodation_cost = accomodation_cost * 0.8
            discount = True
        else:
            discount = False
    
        print("flight cost is $", flight_cost)
        print("")
        if discount == True:
            print("accomodation cost will be 80% because you stayed 3 or more nights")
        print("accomodation cost is $", accomodation_cost)
        print("")
        print("")
        print("total cost is $", flight_cost + accomodation_cost)
        print("")
        print("")
        
        confirm = input("Do you want to confirm this cost? (answer in yes or no): ")
        if confirm == "yes":
            ask = False
            
        else:
            print("")
            print("")
            continue
                      
    