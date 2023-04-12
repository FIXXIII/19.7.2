import time

def timer(seconds):
    print("Timer started for", seconds, "seconds")
    time.sleep(seconds)
    print("Timer ended after", seconds, "seconds")

timer(60)  # запуск таймера на 60 секунд