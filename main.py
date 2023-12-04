# import asyncio
#
# async def async_func(task_no):
#     print(f'...start {task_no}')
#     await asyncio.sleep(3)
#     print(f'...end {task_no}')
#
# async def main():
#
#     task1 = asyncio.create_task(async_func('A'))
#     task2 = asyncio.create_task(async_func('B'))
#     task3 = asyncio.create_task(async_func('C'))
#     await asyncio.wait([task1, task2, task3])
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
# def multiply(a, b):
#     return a * b
#
# import asyncio
# async  def async_function(a):
#     while True:
#         await a
#         a += 1
#
# asyncio.run(async_function(2))
#
# import asyncio
#
# async def count(counter):
#     print(f'Количество записей в списке {len(counter)}')
#     while True:
#         await asyncio.sleep(1 / 1000)
#         counter.append(1)
#
# async def print_every_sec(counter):
#     while True:
#         await asyncio.sleep(1)
#         print(f'- 1 sec passed. Count = {len(counter)}')
#
# async def print_every_5sec():
#     while True:
#         await asyncio.sleep(5)
#         print('5 sec passed')
#
# async def print_every_10sec():
#     while True:
#         await asyncio.sleep(10)
#         print('10 sec passed')
#
# async def main():
#     counter = list()
#     # task1 = asyncio.create_task(count(counter))
#     # task2 = asyncio.create_task(print_every_sec(counter))
#     # task3 = asyncio.create_task(print_every_5sec())
#     # task4 = asyncio.create_task(print_every_10sec())
#     # await asyncio.wait([task1, task2, task3, task4])
#     tast_list = [
#         count(counter),
#         print_every_sec(counter),
#         print_every_5sec(),
#         print_every_10sec()
#     ]
#     await asyncio.gather(*tast_list)
#
#
# asyncio.run(main())
#
# import time
# import asyncio
# async def brewCoffee():
#     print("Start brewCoffee()")
#     await asyncio.sleep(3)
#     print('Finish brewCoffee()')
#     return 'Coffee is ready'
#
# async def toastBage1():
#     print("Start toastBage1()")
#     await asyncio.sleep(3)
#     print('Finish toastBage1()')
#     return 'Toast is ready'
#
# async def main():
#     stat = time.time()
#     # batch = asyncio.gather(brewCoffee(), toastBage1())
#     # result_coffee, result_toast = await batch
#
#     # result_coffe = brewCoffee()
#     # result_toast = toastBage1()
#
#     tast_c = asyncio.create_task(brewCoffee())
#     tast_t = asyncio.create_task(toastBage1())
#     result_coffee = await tast_c
#     result_toast = await tast_t
#
#     end = time.time()
#
#     print(result_coffee)
#     print(result_toast)
#     print(f'spent time = {end - stat:.2f} seconds')
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#
# import time
# import asyncio
#
# async def my_sleep():
#     print('my sleep start')
#     await asyncio.sleep(2)
#     print('my sleep stop')
#
# async def main():
#     print('sleep now')
#     await my_sleep()
#     print('sleep stop')
#
# asyncio.run(main())
# import asyncio
# import http
#
#
# async def download(current_page):
#     url = f'https://catfact.ninja/fact'
#
#     async with http.AsyncClient() as client:
#         r = await client.get(url)
#         if r.status_code == 200:
#             _r = r.json()
#             print(_r.get('fact'))
#         else:
#             print(r.status_code)
#     print(f' {current_page}')
#
# async def main():
#     page_count = int(input("Page count? "))
#
#     current_page = 0
#     task_list = []
#     while current_page < page_count:
#         current_page += 1
#         task = asyncio.create_task(download(current_page))
#         task_list.append(task)
#         # await download(current_page)
#     await asyncio.gather(*task_list, return_exceptions=True)
#     print('Done')
#
# asyncio.run(main())
#
# import asyncio, time
# async def action_1(a, b):
#     print('Значения получены')
#     print('Вносим значение в базу ...')
#     await asyncio.sleep(1)
#     print(f'Результат действия (action 1) равен: {a + b}')
#
# async def action_2(a):
#     print('Значения получены')
#     print('Вносим значение в базу ...')
#     await asyncio.sleep(3)
#     print(f'Результат действия (action 2) равен: {a ** 2}')
#
# async def main():
#     tk_1 = asyncio.create_task(action_1(1, 2))
#     tk_2 = asyncio.create_task(action_2(3))
#     await asyncio.wait([tk_1, tk_2])
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
# import asyncio
#
# async def phone():
#     while True:
#         print('Отвечает на телефонный звонок.')
#         await asyncio.sleep(1)
#
# async def visitors():
#     while True:
#         print('Принимает посетителей.')
#         await asyncio.sleep(2)
#
# async def tickets():
#     while True:
#         print("Бронирует билеты.")
#         await asyncio.sleep(3)
#
# async def schedules():
#     while True:
#         print("Работаем с расписанием встреч.")
#         await asyncio.sleep(4)
#
# async def paperwork():
#     while True:
#         print('Заполняет документы.')
#         await asyncio.sleep(5)
#
# async def main():
#     tasks = [
#         phone(),
#         visitors(),
#         tickets(),
#         schedules(),
#         paperwork(),
#     ]
#
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())