
# import asyncio
#
#
# async def compute(x, y):
#     print("Compute %s + %s ..." % (x, y))
#     await asyncio.sleep(10.0)
#     return x + y
#
#
# async def print_sum(x, y):
#     result = await compute(x, y)
#     print("%s + %s = %s" % (x, y, result))
#
#
# loop = asyncio.get_event_loop()
# tasks = [print_sum(1, 2), print_sum(3, 4)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1) # 这里为啥线程不等待asyncio.sleep(1)执行完
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()