favourite_food = [] #initialize empty list for favourite foods


while True:

    print("Welocome to Favourite Food Manager.")
    print("0. Exit")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View all Favourite Foods")


    option = input("Select an Option: ") #for taking inputs from user


    if option == "0":
        print("Thanks for Using Favourite Food Manager.")
        break

    elif option == "1":
        food = input ("Enter your favourite food name: ")
        favourite_food.append(food)
        print(f"{food} Added Successfully.")

    elif option == "2":
        food = input ("Enter your favourite food name: ")
        favourite_food.remove(food)
        print(f"{food} Removed Successfully.")

    elif option == "3":
        if favourite_food:
            print("Your Favourite Foods: ")
            for index, food in enumerate(favourite_food, start=1):
                print (f"{index}.{food}")
        else:
            print("Food list is empty or didn't add yet!")

    else:
        print("Invalid Inputs!")        


 





