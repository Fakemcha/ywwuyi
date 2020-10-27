import os
import sys
import subprocess
from apps.settings import BASE_DIR, PROJECT_DIR
sys.path.append(BASE_DIR)
from apps.ywwuyi.timedtask.controller import timedtaskController
import time


class TimedtaskRunner(object):
    def __init__(self):
        self.FILE = os.path.abspath(__file__)
        self.PIDFILE = os.path.join(PROJECT_DIR, "tmp", "timedtask.pid")

    def start(self):
        cmd = [
            'python',
            self.FILE,
        ]
        p = subprocess.Popen(cmd)
        with open(self.PIDFILE, 'w') as fpid:
            fpid.write(str(p.pid))

    def stop(self):
        if os.path.exists(self.PIDFILE):
            with open(self.PIDFILE, 'r') as fpid:
                pid = fpid.read()
            cmd = [
                "kill",
                "-9",
                pid,
            ]
            subprocess.Popen(cmd)
        # cmd = [
        #     "rm",
        #     "-f",
        #     self.PIDFILE,
        # ]
        # subprocess.Popen(cmd)

    def restart(self):
        self.stop()
        self.start()


timedtaskRunner = TimedtaskRunner()

if __name__ == '__main__':
    # pass
    timedtaskController.run()
    # while True:
    #     time.sleep(3)
    #     tasks = timedtaskController.get_tasks()
    #     print(tasks)
    #     for t in tasks:
    #         if tasks[t].is_alive():
    #             print("alive")
