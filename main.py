import sqlite3

db = sqlite3.connect('data.db')
base = db.cursor()
base.execute("""CREATE TABLE IF NOT EXISTS workers (name TEXT, age INT, progul INT,salary INT)""")
db.commit()

name = input('Введите инициалы: ')
age = int(input('Введите возраст: '))
progul = int(input('Введите количество смен: ')) - int(input('Введите количество посещенных смен: '))
salary = int(input('Введите оклад: '))


base.execute(f"INSERT INTO workers VALUES (?, ?, ?, ?)", (name, age, progul, salary))
db.commit()

if input('Желаете ли отсортировать по размеру зарплаты?: ') == 'да':
    base.execute("SELECT * FROM workers ORDER BY salary")
    print(base.fetchall())
    db.commit()

if input('Желаете ли отсортировать по количеству прогулов?: ') == 'да':
    base.execute("SELECT * FROM workers ORDER BY progul")
    print(base.fetchall())
    db.commit()

db.close()