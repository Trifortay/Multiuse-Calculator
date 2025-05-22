def fib():
    print("Fibonacci Calculator")
    a=1
    b=1
    n=0

    while n==0:
            try:
                n=int(input("Enter which Fib number you wanna calculate: "))
            except ValueError:
                n=0

    # Use n now for value.
    if n>1:
        for x in range(n-2):
            temp=a+b
            a=b
            b=temp
        print(b)

