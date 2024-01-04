
import subprocess
import os
import time
from typing import List, Dict
import yaml


BASE_PATH = os.getcwd()


# TODO add test
def get_yaml_tasks_params_list() -> List[Dict]:
    tasks_path = f"{BASE_PATH}/tasks"
    complete_file_paths_list = [
        os.path.join(tasks_path, yaml_file) for yaml_file in
        os.listdir(tasks_path)
    ]

    tasks_params_list = []
    for complete_path in complete_file_paths_list:
        with open(complete_path, "r") as f:
            tasks_params_list.append(
                yaml.safe_load(f)
            )
    
    return tasks_params_list


# TODO add test
def run_task(task: dict) -> None:
    execution_method = task.get("execution-method")
    task_path = f'{BASE_PATH}/{task.get("task-path")}'

    subprocess.run(
        [execution_method, task_path]
    )


if __name__ == "__main__":
    while True:
        time.sleep(2)
        for task in get_yaml_tasks_params_list():
            run_task(task)
            print("running")


