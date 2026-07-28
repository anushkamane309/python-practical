print("======TRAFFIC CONTROLLER======")

signal = input("Enter traffic signal color :").lower()

if signal == "red":
    print("Action : STOP")

else:
    if signal == "yellow":
        print("Action : READY")

    else:
        if signal == "green":
           print("Action : GO") 
        else:
             print("Invalid signal color")

