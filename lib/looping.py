#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while (count >= 0):
        if(count == 0):
            print("Happy New Year!")
        else:
            print(count)
        count-=1
    pass

def square_integers(int_list):
    int_list = [num * num for num in int_list]
    return int_list
    pass

def fizzbuzz():
    for i in range(100):
        if ((i + 1) % 3 == 0):
            if ((i + 1) % 5 == 0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif ((i + 1) % 5 == 0):
            if ((i + 1) % 3 == 0):
                print("FizzBuzz")
            else:
                print("Buzz")
        else:
            print((i + 1))
        
    pass
