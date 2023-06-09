import asyncio
import os
import queue
from isolate import Isolate

from service.wobsocket import WebSocketServer
from base.wrap_pb import InfoType

loop = None

run_path = os.getcwd()

def get_loop():
    global loop
    if loop is None:
        loop = asyncio.new_event_loop()
    return loop

# server = websocket.WebSocketServer()
server = WebSocketServer()
task_queue = queue.Queue()

# 运行产生的信息队列
info_queue = queue.Queue()

class Info:
    status: InfoType = InfoType.SUCCESS,
    body = None
    def __init__(self, message: any) -> None:
        self.body = message

class Success(Info):
    def __init__(self, message: any) -> None:
        super().__init__(message)
        self.status = InfoType.SUCCESS

class Error(Info):
    def __init__(self, message: any) -> None:
        super().__init__(message)
        self.status = InfoType.ERROR

class Warn(Info):
    def __init__(self, message: any) -> None:
        super().__init__(message)
        self.status = InfoType.WARN

