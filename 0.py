import os
import time


def decorator(func):
    def wrapper():
        print(f"Running {func.__name__}...")
        time.sleep(2)
        func()
    return wrapper


with open ('grocerylist.txt') as file:
    print("Opening 'grocerylist.txt'...")
    time.sleep(3)
    print(file.read())


@decorator
def more_grocery():
    global category
    more = input(f"Add more {category}: ")
    print(f"Adding: ({more})")
    with open('grocerylist.txt', 'a') as file:
        file.write(f"\n{more}")
    time.sleep(2)
    print(f"Added {more}")


def no_more_grocery():
    print("Closing grocery list...")
    time.sleep(2)
    print("Saved")
    exit()

while True:
    match input("would you like to add anything ?(y/n): "):
        case "y":
            with open('grocerylist.txt', 'a') as file:
                category = input("What category is the new goods you're adding?: ")
                category = category.upper()
                file.write(f"\n---------------- {category}--------------------") 
            more_grocery()
        case "n":
            no_more_grocery()
        case _:
            print("Invalid input")

            
