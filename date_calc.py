import datetime
def date_subtract():
    def date_make(doq):
        doq_list=doq.split("-")
        try:
            actual_date=datetime.date(int(doq_list[0]),int(doq_list[1]),int(doq_list[2]))
        except:
            print("Enter a valid number next time.")
            return 
        return actual_date
        

    print("This tool will let you calculate how long between two dates are.")
    print("Enter two dates seperated by dashes (-), in YYYY-MM-DD format")
    print("Or enter \"exit\" to exit")
    exit_prog=0
    while exit_prog<2:
        try:
            date1=input("Date 1: ")
            if date1=="exit":
                exit_prog=3
                return
        except:
            print("Not a Valid Date")
            exit_prog=3
        actual_date1=date_make(date1)
        exit_prog=1
        if exit_prog==1:
            try:
                date2=input("Date 2: ")
                if date2=="exit":
                    exit_prog=3
                    return
            except:
                print("Not a Valid Date")
                exit_prog=3
            actual_date2=date_make(date2)
        time_diff=actual_date1-actual_date2
        print(f"\nDays left: {time_diff.days}")
        exit_prog=3

        

