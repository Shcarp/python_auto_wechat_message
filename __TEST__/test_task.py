import os
import random
import sys
import time
import schedule

sys.path.append(os.path.join(os.getcwd()))

from src.task.base import Task, TaskConfig
from src.task.execute import PythonExecuteTaskConfig

def generateTask(run_count, time):
    return Task(config=TaskConfig(
            name="test", 
            run_count=run_count, 
            trigger_type="interval", 
            trigger_info={"interval": time}, 
            execute_type="Python", 
            execute_info=PythonExecuteTaskConfig(
                key="test.zip",
                module="py",
                location="local",
                path=os.path.join(os.getcwd(), '__test__', "testData", "test.zip"),
                params={"a": 1, "b": 2}
            )
        )
    )

def testTrigger():
    taskList = []

    for i in range(1, 10):
        task = generateTask(5, i + random.randint(1, 10))
        taskList.append(task)
        task.start()

    task2 = Task(config=TaskConfig(
            name="test", 
            run_count=5, 
            trigger_type="interval", 
            trigger_info={"interval": 4}, 
            execute_type="Python", 
            execute_info=PythonExecuteTaskConfig(
                key="7339de53cee41af98a2109200.0.1.tar.gz",
                module="package",
                location="remote",
                path="http://1.117.56.86:8090/download/7339de53cee41af98a2109200.0.1.tar.gz",
                params={"a": 1, "b": 3}
            )
        )
    )
    task2.start()

    while True:
        schedule.run_pending()
        time.sleep(1)


testTrigger()