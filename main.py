import time
import schedule
import os

def start_minecraft():
        os.system("sudo systemctl start minecraftpeserver.service")
        print("Successfully start minecraftpeserver")

def stop_minecraft():
        os.system("sudo systemctl stop minecraftpeserver.service")
        print("Successfully stop minecraftserver")


schedule.every().day.at("08:00").do(start_minecraft)
schedule.every().day.at("23:00").do(stop_minecraft)
schedule.every().day.at("13:00").do(start_minecraft)
schedule.every().day.at("23:00").do(stop_minecraft)

while True:
        schedule.run_pending()
        time.sleep(1)


