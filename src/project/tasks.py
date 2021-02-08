import asyncio


async def sleepy_task(app, custom_param):
    print('sleep for 5s')
    print(custom_param)
    await asyncio.sleep(5)
    print('woke up!')