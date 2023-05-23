

import asyncio
import os
import ssl
import aiomysql
from loop import loop

__all__ = ["mysql"]

ssl_defaults = ssl.get_default_verify_paths()
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.load_verify_locations(cafile=ssl_defaults.cafile)

async def register():
    '''
    初始化，获取数据库连接池
    :return:
    '''
    try:
        print("start to connect db!")
        POOL = await aiomysql.create_pool(
            host='aws.connect.psdb.cloud',
            port=3306,
            user='w9lcpjt2lci4t6ywjniy',
            password='pscale_pw_wQ0nZ3IBGHGRczI98mD7ZrXkZMmuL8A7A67wP0aiXXV',
            db='sh-sql',
            charset='utf8',
            loop=loop,
            ssl=ctx,
        )
        print("succeed to connect db!")
        return POOL
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    except Exception as ex:
        print(ex)
        print("mysql数据库连接失败：{}".format(ex.args[0]))
        return False

# POOL = register()

# CREATE TABLE task ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL,type VARCHAR(50),status VARCHAR(50),time DATETIME,content TEXT,member VARCHAR(200));
# 初始化数据库
# def init_task_db():
#     with POOL.acquire() as conn:
#         cursor = conn.cursor()
#         try:
#             # 判断任务表是否存在，不存在则创建
#             cursor.execute("SHOW TABLES LIKE 'task'")
#             if (cursor.fetchone() is None):
#                 cursor.execute("CREATE TABLE task ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL,type VARCHAR(50),status VARCHAR(50),time BIGINT,content TEXT,member VARCHAR(200))")
            
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             raise e
#         finally:
#             cursor.close()

# CREATE TABLE wechat_names (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL);
# 初始化数据库
# def init_wechat_names_db():
#     with POOL.acquire() as conn:
#         cursor = conn.cursor()
#         try:
#             cursor.execute("SHOW TABLES LIKE 'wechat_names'")
#             if (cursor.fetchone() is None):
#                 cursor.execute("CREATE TABLE wechat_names (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL)")
            
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             raise e
#         finally:
#             cursor.close()

# init_task_db()
# init_wechat_names_db()

# task_module = TaskMySql()
# wechat_name_module = WechatNamesMySql()


