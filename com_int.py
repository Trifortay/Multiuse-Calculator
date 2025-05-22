import math

def money():
    def redo():
        print("\nPlease enter a valid number.")

    valid_money=False
    valid_unit=False
    valid_meas=False
    valid_rate=False
    
    while valid_money==False:
        ini_money=input("Enter money deposited: $")
        if not ini_money.isalpha():
            s2_money=float(ini_money)
            valid_money=True
        else:
            redo()
    
    while valid_unit==False:
        unit=int(input("Do you wanna input days (1) or years (2)? "))
        if unit in [1,2]:
            unit=int(unit)
            valid_unit=True
        else:
            redo()
    
    while valid_meas==False:
        meas=input("Please enter the amount of days to be compounded: " if unit==1 else "Please enter the amount of years to be compounded: ")
        if not meas.isalpha():
            meas=float(meas)
            valid_meas=True
        else:
            redo()
    
    while valid_rate==False:
        ini_rate=input("Please input the rate in a percentage format without the %: ")
        if not ini_rate.isalpha():
            rate=float(ini_rate)/100
            valid_rate=True
        else:
            redo()
    
    total_money=s2_money*(1+rate)**meas
    print(f"The Total Money Compounded is ${total_money}")
    


