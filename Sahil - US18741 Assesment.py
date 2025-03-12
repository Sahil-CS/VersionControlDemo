def print_receipt(spacecraft, hire_duration, pilot_needed, total_cost, passengers):
    #Print the receipt with details of the hire.
    print("\n========================================")
    print("              RECEIPT")
    print("========================================")
    print(f"    Spacecraft: {spacecraft}")
    print(f"    Days Hired: {hire_duration}")
    print(f"    Passengers: {passengers}")
    print(f"    Pilot Needed: {pilot_needed}")
    print("----------------------------------------")
    print(f"    Total Cost     : ${total_cost}")
    print("========================================\n")
   
    #Ask if the user wants to hire another spacecraft.
    restart = ""
    while restart not in ["y", "n", "no", "yes"]:
        restart = input("Would you like to hire another spacecraft? (y/n): ").strip().lower()

        if restart == "y" or restart == "yes":
            main()

        elif restart == "n" or restart == "no":
            exit()

        else:
            print("")
            print("Please enter a valid input y, n, yes, no")

 
   

#Spacecraft rental prices per day.
blue_origin_price = 8000
rocket_lab_price = 10000
spacex_falcon_price = 5000

#Available spacecraft models.
blue_origin_available = 3
rocket_lab_available = 3
spacex_falcon_available = 3

def main():
    print("\n******** Welcome to Sahil's Spacecraft Hire ********\n")
   
    #list of available spacecrafts with their prices and availability.
    spacecraft_options = {
        1: ("Blue Origin New Shepard", blue_origin_price, blue_origin_available),
        2: ("Rocket Lab Photon", rocket_lab_price, rocket_lab_available),
        3: ("SpaceX Falcon 9", spacex_falcon_price, spacex_falcon_available),
        4: ("Exit", 0, 0)
    }
   
    while True:
        #Display available spacecrafts.
        print("\nAvailable Spacecrafts:\n")
        for num, (name, price, available) in spacecraft_options.items():
            print(f"{num}. {name} - ${price}/day (Available: {available})" if num != 4 else f"{num}. {name}\n")
       
        #Get user selection.
        try:
            choice = int(input("Select a spacecraft (1-4): "))
            if choice == 4:
                print("\nThank you for using the Spacecraft Hire Program! Goodbye.")
                exit()
            elif choice in spacecraft_options and spacecraft_options[choice][2] > 0:
                selected_spacecraft, daily_price, _ = spacecraft_options[choice]
                break
            else:
                print("\nInvalid choice. Try again.")
        except ValueError:
            print("\nPlease enter a number between 1 and 4.")
   
    while True:
        #Get hire duration.
        try:
            hire_duration = int(input("\nEnter hire duration (1-30 days): "))
            if 1 <= hire_duration <= 30:
                break
            print("\nDuration must be between 1 and 30 days.")
        except ValueError:
            print("\nEnter a valid number.")
   
    while True:
        #Validate pilot input.
        pilot_input = input("\nDo you need a pilot? (yes or y/no or n): ").strip().lower()
        if pilot_input in ["yes", "y", "no", "n"]:
            pilot_needed = pilot_input in ["yes", "y"]
            pilot_cost = 500 * hire_duration if pilot_needed else 0
            break
        else:
            print("\nPlease enter 'yes/y' or 'no/n'.")
   
    while True:
        #Get number of passengers.
        try:
            passengers = int(input("\nEnter number of passengers (1-10): "))
            if 1 <= passengers <= 10:
                passenger_cost = 500 * passengers * hire_duration
                break
            print("\nPassengers must be between 1 and 10.")
        except ValueError:
            print("\nEnter a valid number.")
   
    #Calculate total cost.
    total_cost = (daily_price * hire_duration) + pilot_cost + passenger_cost
   
    #Print the receipt.
    print_receipt(selected_spacecraft, hire_duration, pilot_needed, total_cost, passengers)

#Restart the program.
main()
