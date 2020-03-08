"""calculates the cost of trip"""

#set function for display lists

def display(a):
    """display the lists"""
    length = len(a)
    for n in range (0,length):
        print(n+1, a[n])
        
#list for departure location
departure = ["Auckland", "Wellington", "Christchurch"]
        
#list for destination location
destinations = ["Sydney", "Tonga", "Shanghai", "London"]


          
#set flight cost to 0
flight_cost = 0

#set accomodation cost to 0
accomodation_cost = 0

#sey ask to true
ask = True

#while loop until user confirm
while ask == True:
    
    #set menu to true
    menu = True
    
    #while loop to make sure user input from option
    while menu == True:
        
        #display departure location option
        display(departure)
        print("")
        
        #ask for input
        depart = input("Enter a number for location that you are departuring: ")
        print("")
        print("")
    
        
        #add domestic cost to flight cost
        #if user enter a correct input, set menu to false
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
    
    
    #set menu to true
    menu = True
    
    #while loop to make sure user enter input from menu
    while menu == True:
        
        #display locations for distination
        display(destinations)
        print("")
        
        #ask user for input     
        destination = input("Enter a number for location that you want to go: ")
        print("")
        print("")
        
        #add international cost to flight cost
        #set menu to false when user input from menu
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
    
    #set menu to true
    menu = True
    
    #while loop to make sure user input from menu
    while menu == True:
        
        #set integer to true
        integer = True
        
        #while loop to make sure user enter an integer
        while integer == True:
            try:
                #ask user for input
                stay = int(input("Enter a number of nights you are staying: "))
                        
                integer = False
                        
            except ValueError:
                print("Enter an integer")
                        
            print("")
            print("")
            
        if stay <= 0:
            print("You should be staying at least one night")
        
        #add accomodation cost to accomodation cost
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
        
    #discount the accomodation cost if user is staying for 3 or more nights
    if stay >= 3:
        accomodation_cost = accomodation_cost * 0.8
        discount = True
            
    else:
        discount = False
        
    #print flight cost
    print("flight cost is $", flight_cost)
    print("")
        
        
    if discount == True:
        print("accomodation cost will be 80% because you stayed 3 or more nights")
            
    #print accomodation cost
    print("accomodation cost is $", accomodation_cost)
    print("")
    print("")
        
    #print total cost
    print("total cost is $", flight_cost + accomodation_cost)
    print("")
    print("")
        
    ask2 = True
    #while loop to make sure user answer in yes or no
    while ask2 == True:
        #ask user to confirm
        confirm = input("Do you want to confirm this cost? (answer in yes or no): ")
        if confirm == "yes":
            ask = False
            ask2 = False
                
        elif confirm == "no":
            ask2 = False
            print("")
            print("")
            
        else:
            print("")
            print("answer in yes or no")
            print("")
            
                      
    