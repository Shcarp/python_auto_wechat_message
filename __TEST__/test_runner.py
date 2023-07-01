import os
import sys
sys.path.append(os.path.join(os.getcwd()))
from src.task.execute_script.python import PythonRunner

def testSourceCode():
    path = os.path.join(os.path.dirname(__file__), "./" ,"testData/test.zip")
    runner = PythonRunner.getInstance("py", path=path)
    runner.run({"a": 1, "b": 2})

def testBytesCode():
    path = os.path.join(os.path.dirname(__file__), "./" ,"testData/testbytes.zip")
    runner = PythonRunner.getInstance("pyc", path=path)
    runner.run({"a": 1, "b": 2})

def testPackage():
    path = os.path.join(os.path.dirname(__file__), "./" ,"testData/addNum-0.0.1.tar.gz")
    runner = PythonRunner.getInstance("package", path=path)
    runner.run({"a": 1, "b": 2})

testSourceCode()
testBytesCode()
testPackage()

'''
myproject
├── __test__
│   ├── testDataxw
|   |   ├── test.zip
|   |   ├── testbytes.zip
|   |   └── addNum-0.0.1.tar.gz
│   ├── test_task.py
│   └── test_runner.py
├── addNum
│   ├── __init__.py
│   └── addNum.py
├── cache
│   └── test.pyc
├── config
│   └── config.toml
├── src
|   ├── task
|   |   ├── base.py
│   ├── __init__.py
│   └── main.py
└── app.py
'''

