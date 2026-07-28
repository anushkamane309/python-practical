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

'''signal = input("Enter traffic signal color :").lower()
vehicle =input("Enter Vehicle is present?(yes/no) :").lower()
if signal == "red":
    if signal =="red"and vehicle =="yes":
      print("Action : STOP")
    else:
       print ("No Vehicle Wait")
        
else:
    if signal == "yellow":
        if signal =="yellow"and vehicle =="yes":
         print("Action : READY")
    else:
     if signal == "green":
            if signal =="green"and vehicle =="yes":
            
             print("Action : GO") 
            else:
             print("Invalid signal color")'''