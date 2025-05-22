
def countdown():
    import time

    ini_time=input("Input a time in HH:MM:SS format including the [:]: ")
    timelist=ini_time.split(":")
    hours=0
    minutes=0
    seconds=0
    try:
        hours=int(timelist[0])
        minutes=int(timelist[1])
        seconds=int(timelist[2])
        total=hours*3600+minutes*60+seconds

        for x in reversed(range(1,total+1)):
            x_hours=x//3600
            x_minutes=(x % 3600) // 60
            x_seconds= x % 60
            print(f"Time Left: {x_hours}:{x_minutes:02d}:{x_seconds:02d}")
            time.sleep(1)  

    except ValueError:
        print("Enter a valid time in the valid format!")
        time.sleep(3)
    
    print("Time's Up!")
    time.sleep(1)

