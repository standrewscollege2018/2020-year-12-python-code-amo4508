"""Storing books - Arisa Mori """

#Bookstore - store books
#Arisa Mori
#set function for displaying list
def display():
    """displaying books in the list"""
    length = len(books)
    for n in range(0,length):
        print(n+1, books[n][0],"-",books[n][1],"-$",books[n][2])
        
#set list for books
books = [["Harry Potter", "J.K.Rowling", 16], ["Romeo and Juliet", "William Shakespeare", 20], ["The old man and the sea", "Ernest Hemingway", 13]]

#set ask to true to keep conitnue
ask = True

        
#display list
display()
print("")
print("")

#while loop to continue
while ask == True:
    option = True
    
        
    #print options
    print("1. Add information of a book")
    print("2. Delete information of a book")
    print("3. Change information of a book")
    
    print("")
    print("")
    
    #while loop for make sure user enter an option from menu
    while option ==True:
        
        #ask for an option
        action = input("Enter a number to select a option that you want to do: ")
        print("")
        print("")
    
        #if statements for selecting option
        if action == "1":
        
            #ask users for inputs
            name = input("Enter a name of book that you want to add: ")
            print("")
            author = input("Enter a author of book that you want to add: ")
            print("")
            
            integer = True
            #while loop for make sure user enter an integer
            while integer == True:
                try:
                    price = int(input("Enter a price of book that you want to add: "))
                    print("")
                    integer = False
                except ValueError:
                    print("")
                    print("Answer in integer")
                print("")
            
            #add information to list
            books.append([name, author, price])
            
            option = False
        
        
        elif action == "2":
            integer = True
            
            #while loop to make sure user enter an integer
            while integer == True:
                try:
                    
                    #ask users for an input
                    delete = int(input("Enter a number of book that you want to delete: "))
                    print("")
        
                    #delete information from list
                    del(books[delete - 1])
                    integer = False
            
                    option = False
                    
                except ValueError:
                    print("")
                    print("Enter a number between 1-3")
                    print("")
        
        elif action == "3":
            integer = True
            
            #while loop to make sure user enter an integer
            while integer == True:
                try:
                    
                    #ask users for inputs
                    change = int(input("Enter a number of book that you want to change: "))
                    print("")
                    integer = False
                    
                except ValueError:
                    print("")
                    print("Enter a number betwee 1-3")
                    print("")
            
            #ask user for name of book
            name = input("Enter a name of book that you want to change to: ")
            print("")
            
            #ask user for name of author
            author = input("Enter a author of book that you wnat to change to: ")
            print("")
            
            integer = True
            
            #while loop to make sure user enter an integer
            while integer == True:
                try:
                    
                    price = int(input("Enter a price of book that you want to change to: "))
                    print("")
                    integer = False
                    
                except ValueError:
                    print("Enter an integer")
                    print("")
        
            #change information on list
            books[change-1] = [name, author, price]
            
            option = False
            
        else:
            print("Please enter a number between 1 and 3")
            
            print("")
            print("")
            display()
            
        print("")
    
    #display list
    display()
    print("")
    print("")
    
    #ask if users want to continue
    ask3 = True
    while ask3 == True:
        ask2 = input("Do you want to continue? (yes or no): ")
        print("")
        print("")
    
        if ask2 == "yes":
            ask = True
            ask3 = False
        
        elif ask2 == "no":
            ask = False
            ask3 = False
            
        else:
            print("")
            print("Answer in yes or no")
            print("")

