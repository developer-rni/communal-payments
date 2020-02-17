# Тестовый файл для проверки работы с базой данных
import sqlite3, sys

# Подключение/создание БД с статичными даными
def sqlite_create_db():

# Подключение/создание БД с динамическими данными

    # соединяемся с бд, если нету создается новая с таким же именем
    con = sqlite3.connect('./data/data_cp.db')

    # создаем объект курсора
    cur = con.cursor()


    # добовляем данные в таблицу
    # UPDATE имя_таблицы SET имя_столбца = новое_значение WHERE условие
    # cur.execute('UPDATE general_total_to_pay SET jan_general_total=2994 WHERE year=2020') # работает
    cur.execute('UPDATE "2020_t13" SET water_this_month=35 WHERE month="jan"') # работает
    # cur.execute("UPDATE 2020_t13 SET water_this_month=? WHERE month=?", (name,category_id)) # name и category_id - переменные



    # подтверждаем внесенные изменения
    con.commit()

    cur.close() # удаляем курсор
    con.close() # разрываем соединение с базой

# запуск
sqlite_create_db()
