import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def select_all_cities(conn):
    sql = '''SELECT * FROM cities'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

connection_to_db = create_connection('hwsql2.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')
    print('Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
    select_all_cities(connection_to_db)

city_id = int(input("Введите id города: "))
if city_id == 0:
    exit()
for row in cursor.execute("SELECT employees.first_name, employees.last_name, countries.title, cities.title, cities.area FROM employees JOIN cities ON employees.city_id = cities.id JOIN countries ON cities.country_id = countries.id WHERE cities.id = ?", (city_id,)):
    print(row[0], row[1], row[2], row[3], row[4])
    
    connection_to_db.close()

