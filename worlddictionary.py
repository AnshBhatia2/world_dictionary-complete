world_dictionary = {

}
#making infinite loop
while True :
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")

    choice = int(input("Enter your choice (1-5) : "))
    if choice == 1 :
        country = input("What is the name of your country ")
        capital = input("What is the country's capital ")
        world_dictionary[country]=capital
        print("Data Added to dictionary")
        print(world_dictionary)

    elif choice == 2 :
        print(world_dictionary.keys())

    elif choice == 3 :
        print(world_dictionary.values())

    elif choice == 4 :
        country = input("What is the name of the country? ")
        print(world_dictionary[country])

    elif choice == 5 :
        deletion = input("Which country would you like to delete? ")
        del(world_dictionary[deletion])
        print(world_dictionary)