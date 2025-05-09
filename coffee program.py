# demonstrate how to use while loops and if statements
# luke searancke
# 9 may 2025
# version 1

# whiles loop
keep_going = "" # the variable contains an empty string
while keep_going == "":

    like_to_smoke = input("do you smoke?")

    if like_to_smoke == "yes":
        print("why? are you depressed or do you think its cool?")
        keep_going = "end"

    if like_to_smoke == "no":
        print("good for you, your lungs ant dieing")
        keep_going = "end"