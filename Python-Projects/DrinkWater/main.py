import time
from plyer import notification
while True:
    print("Drink water")
    notification.notify(title="Please Drink Water", message="It's time to drink water!", timeout=10)
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)