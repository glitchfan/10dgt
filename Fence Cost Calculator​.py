# ask the person what the width, height and cost of the fences
def num_check():
        keep_going = ""
        while keep_going == "":
            while True:
                try:
                    width = float(input("width: "))
                    if width > 0:  # You can add additional validation criteria here
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                try:
                    height = float(input("height: "))
                    if height > 0:  # You can add additional validation criteria here
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            while True:
                try:
                    cost = float(input("cost peer meter: "))

                    if cost > 0:  # You can add additional validation criteria here
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:            
                    print("Invalid input. Please enter a valid integer.")

                    # show the cost of the fence

            print(width)
            print(height)
            print(cost)
            sum2 = round(((width * 2) + (height * 2)), 2)
            print()
            print(f"your perimeter is {sum2}m")
            sum3 = round((sum2 * cost), 2)
            print(f"${sum3}")
                                
            keep_going = input("press enter to keep going or any key to quit") 
            print()
            
            print("thank you for useing my program insted of the other dumb ones")

num_check()