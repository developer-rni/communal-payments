# Тестовый файл для проверки работы с базой данных
import sqlite3

# Подключение/создание БД с статичными даными
def sqlite_update_db():

# Подключение/создание БД с динамическими данными

    # соединяемся с бд, если нету создается новая с таким же именем
    con = sqlite3.connect('./data/data_cp.db')

    # создаем объект курсора
    cur = con.cursor()

    year_addr = '2020_t13'
    # print(year_addr)
    payment_type = 'water_to_pay'
    # print(payment_type)
    number = 697.32
    # print(number)
    what_month = 'jan'
    # print(what_month)

    # добовляем данные в таблицу
    # UPDATE имя_таблицы SET имя_столбца = новое_значение WHERE условие
    # cur.execute('UPDATE general_total_to_pay SET jan_general_total=2994 WHERE year=2020') # работает
    # cur.execute('UPDATE "2020_t13" SET water_this_month=31 WHERE month="jan"') # работает
    cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type, number, what_month))


    # # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    # cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
    #
    # # Получаем результат сделанного запроса
    # results = cursor.fetchall()
    # results2 =  cursor.fetchall()
    #
    # print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
    # print(results2)  # []


    # подтверждаем внесенные изменения
    con.commit() # .rollback() для отмены изменений

    cur.close() # удаляем курсор
    con.close() # разрываем соединение с базой

# sqlite_update_db() #запуск