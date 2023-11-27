command=""
started = False
while True:
    command = input("-> ").lower()
    if command == "start":
        if started:
            print("Car is Already Started")
        else:
            started = True
            print("Car Started")
    elif command ==  "stop":
        if not started:
            print("Car is Already Stopped")
        else:
            started =  False
            print("Car Stoppped")
    elif command == "help":
        print('''
start -> Start the Car
stop ->  Stop the Car
quit -> Quit Game
              ''')
    elif command == "quit":
        break
    else:
        print("Enter a correct option")    
    