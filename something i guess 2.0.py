# from turtle import width
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


            sum = round((width * height), 2)
            sum2 = round(((width * 2) + (height * 2)), 2)
            print()
            print(f"your area is {sum} units")
            print(f"your perimeter is {sum2} square units")
                                
            keep_going = input("press enter to keep going or any key to quit") 
            print()
            
            print("thank you for useing my program insted of the other dumb ones")

num_check()