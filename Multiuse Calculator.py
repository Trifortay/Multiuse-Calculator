#import keyboard    
import date_calc   # Date Calculator
import com_int     # Compound Interest Calculator
import fib         # Fibonacci Calc
import timer       # Countdown Timer
# import hello.tri   # About Page



# This will be used for The amount of tools currently, may change due to updates.
tools=[1,2,3,4,9]            

# Ask for which tool to use
valid_tool=False

run_forever=True

while run_forever==True:
    print("Welome to Trifortay's Multiuse Calculator")
    print("Please select something to do.")
    print("1. Date and Time Calculator")
    print("2. Compound Interest Calculator")
    print("3. Fibonacci Calulator")
    print("4. Timer")
    print("9. About the dev")
    while valid_tool==False:
        try:
            selected_tool=int(input("Selection: "))
            if selected_tool in tools:
                valid_tool=True
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")
    
    if selected_tool == 1:
        date_calc.date_subtract()
        valid_tool=True
    if selected_tool == 2:
        com_int.money()
        valid_tool=True
    if selected_tool == 3:
        fib.fib()
        valid_tool=True
    if selected_tool == 4:
        timer.countdown()
        valid_tool=True
        
    if selected_tool == 9:
        hello=open("hello.tri","r")
        print(hello.read())
        hello.close()

    valid_tool=False
    run_again=input("\nUse some more (y/n):")
    if run_again=="y":
        run_forever=True
    else:
        run_forever=False
        print("k bye")
        