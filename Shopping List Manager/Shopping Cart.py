'''
Sijjad Khalid
Shopping List Manager
'''

# Welcome user to application
print("Welcome to the Shopping List Manager application!")
shoppingList = {"Monday": ["Milk, Eggs"], "Tuesday": ["Butter"]}


# Display menu
def displayMenu():
    print("\nMain Menu: ")
    # Store menu options into string array
    menuItems = ["Create a new Shopping List",
                 "Add items to Shopping List",
                 "Delete Shopping List",
                 "Display Shopping lists",
                 "Exit"]

    # Loop through the string array to display menu
    for counter, options in enumerate(menuItems, start=1):
        # counter display number in front of options
        menu = "\t" + str(counter) + ") " + str(options)
        print(menu)


def displayCurrentShoppingList():
    print("\nHere are your shopping lists: \n")
    counter = 0
    for lists, items in shoppingList.items():
        counter = counter+1
        # attach a counter to list to keep track of list number
        print("List "+str(counter)+":")
        print("{} \n {} \n".format(lists, items))


def createNewList():
    inputListName = input("Enter a List name: ").title()
    print(inputListName)
    # conditional checks if list already exists
    if shoppingList.get(inputListName) is None:
        shoppingList[inputListName] = []
        displayCurrentShoppingList()
    else:
        print("This Shopping List already exists.")


def addNewItem():
    inputList = input("Enter Shopping List name: ").title()
    # Use conditional to validate user input
    if shoppingList.get(inputList) is not None:
        userChoice = int(input("    1) Add Item\n    2) Exit\n"))
        # loop until user wants to stop adding items
        while userChoice == 1:
            newItem = input("Enter the item you wish to add: ").title()
            shoppingList.setdefault(inputList, []).append(newItem)
            userChoice = int(input("    1) Add Item\n    2) Exit\n"))
    else:
        print("\nThis shopping list does not exist.")
    displayCurrentShoppingList()


def removeShoppingList():
    popList = input("Enter Shopping list you wish to remove: ").title()
    # Use conditional to validate user input
    if shoppingList.get(popList) is not None:
        # drop the Shopping list that is inputted
        shoppingList.pop(popList)
        print(popList + " has been removed")
        # display shopping list method
        displayCurrentShoppingList()
        pass
    else:
        print("\nThis shopping list does not exist.")


displayCurrentShoppingList()
# Ask user for input
displayMenu()
userInput = input("\nEnter a valid option: ")

# Only stay within the loop if input is not 5
while userInput != "5":
    if userInput == "1":
        createNewList()
    elif userInput == "2":
        addNewItem()
    elif userInput == "3":
        removeShoppingList()
    elif userInput == "4":
        displayCurrentShoppingList()
    elif userInput == '5':
        exit()
    else:
        print("\nInvalid Entry")
    displayMenu()
    userInput = input("\nEnter a valid option: ")

print("\nThank you for using the Shopping List Manager application!")