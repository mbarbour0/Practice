# make a list to hold onto our items.
shopping_list = []
# print out instructions on how to use the app
print("What should we pickup at the store?")
print("Enter 'DONE' to stop adding items.")
# ask for new items
while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    # add new items to our list
    shopping_list.append(new_item)

# be able to quit the app
# print out the list
print("Here's your list:")
for item in shopping_list:
    print(item)