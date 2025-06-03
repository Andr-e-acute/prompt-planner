import datetime

def get_current_time():
    now=datetime.datetime.now()
    return now.strftime("%a,%d %b %y - %H:%M")
def get_user_input():
    print("What would you like to get done today?")
    user_input= input("> ")
    return user_input

if __name__ == "__main__":
    print("Current time:", get_current_time())
    
    tasks = get_user_input()
    print("\nYou want to do:")
    print(tasks)