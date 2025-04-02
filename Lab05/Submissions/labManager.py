# Author: Mayank Kumar Pokhriyal
# Date: 27th Feb 2025
# Description: This program Adds upto 5 equipments and remove equipments and display in the Laboratory
lab = []

print("Welcome to the inventory manager for your laboratory!")

while True:
    print("\nYou can choose from the following options:")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")

    choice = input("What would you like to do: ").strip()

    try:
        choice = int(choice)
    except ValueError:
        print(f"{choice} was not a valid option. Please try again")
        continue

    if choice == 1:
        if len(lab) >= 5:
            print("Your laboratory cannot support any more equipment!")
        else:
            equipment = input("What would you like to add to the laboratory: ").strip()
            lab.append(equipment)
            print(f"{equipment} has been added")

    elif choice == 2:
        equipment = input("What would you like to remove from the laboratory: ").strip()
        if equipment in lab:
            lab.remove(equipment)
            print(f"{equipment} has been removed")
        else:
            print(f"{equipment} was not present and could not be removed")

    elif choice == 3:
        if not lab:
            print("Your laboratory is currently empty.")
        else:
            print("Your laboratory currently contains:", end=" ")
            for item in lab:
                print(item, end=" ")
            print()

    elif choice == 4:
        print("Good luck on your journey of discovery!")
        break

    else:
        print(f"{choice} was not a valid option. Please try again")