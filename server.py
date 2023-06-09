import service.task
import service.wechat
import service.common
from module.register import register
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from module.task import TaskMySql
from module.wechat import WechatNamesMySql
from globals import Info, get_loop, server, info_queue, InfoType, task_queue
from base.wrap_pb import InfoType

loop = get_loop()
scheduler = AsyncIOScheduler(event_loop=loop)

async def init_task(regsitertime, task_module):
    task_list = await task_module.get_all_status_task(2)

    for item in task_list:
        regsitertime.add({
            "id": item[0],
            "name": item[1],
            "type": item[2],
            "time": item[4],
            "content": item[5],
            "member": item[6].split(","),
        })

@scheduler.scheduled_job('interval', seconds=5)
async def send_server_message():
    try:
        message = info_queue.get_nowait()
        if (isinstance(message, Info)):
            await server.push(message.status, "info", message.body)
        else:
            await server.push(InfoType.WARN, "other", message)
    except Exception as e:
        if (e.__class__.__name__ != "Empty"):
            print(e)
        pass

@scheduler.scheduled_job('interval', seconds=5)
async def report_block_num():
    try:
        await server.push(InfoType.SUCCESS, "block_num", task_queue.qsize())
    except Exception as e:
        print(e)
        pass

def run_server(regsitertime):
    pool = loop.run_until_complete(register())

    task_module = TaskMySql(pool)
    wechat_name_module = WechatNamesMySql(pool)

    async def init_task_func(task_module):
        server.addModule("task", task_module)
        await init_task(regsitertime, task_module)
    
    async def init_wechat_name_func(wechat_name_module):
        server.addModule("wechat", wechat_name_module)

    loop.run_until_complete(task_module.init_sql(init_task_func))
    loop.run_until_complete(wechat_name_module.init_sql(init_wechat_name_func))

    server.addModule("registerTime", regsitertime)
    try:
        scheduler.start()
        loop.run_until_complete(server.run())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("server start error: {}".format(e))
    finally:
        scheduler.shutdown()
        loop.run_until_complete(pool.close())
        loop.close()

