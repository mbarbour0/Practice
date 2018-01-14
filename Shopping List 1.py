shopping_list = []
print("What should we pickup at the store?")
def show_help():
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list.
    Enter 'REMOVE' to delete an item from your list.
    """)
def show_list():
    
    print("Here's your list:")
    
    for index, item in enumerate(shopping_list, 1):
        print("{}. {}".format(index, item))

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()
        
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
        
show_help()

while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()