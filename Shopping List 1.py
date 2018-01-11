slist = []
while True:
    item = input("\n>>>Enter an item to add it to your shopping list\n>>>To view your shopping list enter VIEW\n>>>To remove an item, type REMOVE\n>>>Type DONE to quit: ")
    if item == "DONE":
        break
    elif item == "VIEW":
        print("\nYour current list is: ")
        for i in slist:
            print(i)
    elif item == "REMOVE":
        ritem = input("Please enter an item to remove it from your shopping list: ")
        if ritem in slist:
            slist.remove(ritem)
            print("\nYou have removed {} from your shopping list.".format(ritem))
        else:
            print("\nThe item was not found on your list")
    else:
        slist.append(item)
        numcount = 1
        print("\nYour list has been updated with {} and is now:".format(item))
        for i in slist:
            print(str(numcount) + ". " + i)
            numcount += 1