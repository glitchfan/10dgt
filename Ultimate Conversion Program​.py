def num_check():
        keep_going = ""
        while keep_going == "":
            while True:
                try:
                    time = float(input("seconds: "))
                    if time > 0:  # You can add additional validation criteria here
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                try:
                    distance = float(input("distance: "))
                    if distance > 0:  # You can add additional validation criteria here
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            while True:
                try:
                    mass = float(input("mass: "))

                    if mass > 0:  # You can add additional validation criteria here
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:            
                    print("Invalid input. Please enter a valid integer.")

                    # show the cost of the fence
            hours = round(time/3600, 2)
            print(((f"{time} seconds = {hours} hours")))
            print(((f"{distance}mm = {distance / 1000}m")))
            print(((f"{mass}g = {mass / 1000}kg")))
            
            print()
  
                                
            keep_going = input("press enter to keep going or any key to quit") 
            print()
            
            print("thank you for useing my program insted of the other dumb ones")

num_check()