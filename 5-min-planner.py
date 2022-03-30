def the_date():
    print("Enter the date for when you will complete these task")
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    year = input("Enter the year: ")
    print(f"{month} {day} {year}")

the_date()

def task_list():
    task1 = input("Task 1: ")
    time1 = input("Task 1 Time length: ")
    try:
        val = int(time1)
    except ValueError:
        print("That's not an int!")
    else:
        print(f"{task1} : {time1}mins")
    


task_list()