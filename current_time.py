# filename: current_time.py

from datetime import datetime

def show_current_time():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    show_current_time()
