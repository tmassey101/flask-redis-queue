# project/server/main/tasks.py


import time


def create_task(task_type):
    time.sleep(int(task_type) * 2)
    return True