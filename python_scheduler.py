
import subprocess
import os
import time


def run_scheduler():
    subprocess.run(["python", f"{os.getcwd()}/python/hello.py"])


if __name__ == "__main__":
    while True:
        time.sleep(2)
        run_scheduler()
        print("running")


