# 23.08
# упрощение оспользования баз данных, by MaxGyverTech
import sqlite3

from database.database import DB
from database.fields import *

# создать БД
# (название файла, нужен ли вывод к терминал(по умолчанию False))
db = DB('data.db', debug=True)

# кортеж со столбцами таблици тире их типом данных
# посмотреть можно тут http://unetway.com/tutorial/sqlite-type-data/
# table_dict = {
#     'name': 'TEXT',
#     'id': 'BIGINT'
# }

struct = [TextField('name'), IntegerField('id')]
print(struct)
# создать таблицу
# (имя таблицы, кортеж структуры таблицы)
# db.create_table(table='users', structure=table_dict)
db.create_table(table='users', structure=struct)
# проверить еслть ли такая запись в таком то столбце, возвращает false true
# (столбец, значение для поиска)
if not db.have_write('id', str(0)):
    # и записать данные
    # не актульно(MАССИВ данных для ваписи,важно что в таком же порядке как и в таблице)
    # вместо массива просто все параметры через запятую
    db.write('max', 0)

# получить всю таблицу, 23.08, метод работает плохо
print(db.get_all())

# UPD 25.08: во всех функциях где уместно добавлен НЕОБЯЗАТЕЛЬНЫЙ параметр 'table' для определения таблицы,
# по умолчанию работает с последне таблицой. Теперь необязательные параметры помечаю при помощи "*"

# UPD 25.08: названия аргументов сделаны более интуитивно понятными

# UPD 25.08: добавлен метод изменения записи

db.write('света', 2)  # для проверки
# (значение на которое изменяем, значение по которому ищем какую запись изменить, столбец в котором изменям,
# *(необязательно)столбец покоторому мы можем искать(по умолчанию тот же в который записываем данные),*таблица)
db.edit('egor', 'max', 'name')
db.edit(value='катя', id_value='2', column='name', id_column='id', table='users')

# UPD 26.08: добавлена функция удаления записи
db.write('ivan', 10)  # для проверки

# просто для прикола и что бы видеть промежуточный результат
if input('Delete?(Y/N)').lower() == 'y':
    # (значение по которому искать, столбец по которому искать, *таблица)
    db.delete('ivan', 'name')
    # b nen vyt cnfkj ktym gthtrk.xfnm zpsr =)
    db.write('kto to', 666)
    # поодробней ага
    db.delete(id_value=666, id_column='id', table='users')

# 26.08 не понимаю как сделать функцию получения

# всё ещё-.-

# UPD 26.08: ВСЁ, функция поиска сделана

print(db.get_line('egor', 'name'))  # параметры смотрите ниже

# запустите код ещё раз вы создадите вторую катю это важно

# ну что: (значение по которому ищем, столбец по которому ищем,*можно получить не всю строку а конкретный параметр из
# неё(по умолчанию вся строка), *можно ли получить НЕ одну строку(по умолчанию только одну)(ДА ДА функция называется
# получитьстрокУ но может вернуть несколько строк)),*таблица
a = db.get_line(id_value='катя', id_column='name', getval='id', returnone=False, table='users')
print(a)

# тестирую
print(db.get_all())

# UPD 26.08: функция получить всё наконец то работает

# UPD 28.08: пакет упакован и загружен в PyPi !!!

# UPD 31.08: добавлен метод получения столбцов, это было трудно
print(db.get_columns(table='users'))

# UPD 31.08: добавлен метод для получения списка таблиц, пришлось попотеть
print(db.get_tables())

# UPD 31.08: добавлен метод установки таблицы по умолчанию, по умолчанию она уже устонавливается при создании
db.set_default_table('users')

# много где добавлен и исправлен debug

# МЫ НЕ УКАЗЫВАЛИ ЭТОТ СТОЛБЕЦ А ОН ЕСТЬ
print(db.get_line(1, 'rowid'))

# UPD 04.09 для getall добавлен параметр value
print(db.get_all(value='name'))

# UPD 05.09 удаление таблицы
db.create_table('abc', struct)  # автоматически ставится по умолучанию
db.del_table()
db.create_table('cba', struct)
db.del_table(table='cba')

db.set_default_table('users')

print(db.get_columns())
# UPD 05.09 добавлен метод получения типа данных столбца
print(db.get_columns_type())
# полность переработан метод получения типов столбцов

# UPD 15.10 все методы переименовыны на читабельны(это было долго)

# UPD 15.10: добавдены поля, больше словарь с типами не нужен. Система создания таблиц всё ещё кривая
# TextField, IntegerField,RealField,BlobField,NoneField, CustomField
# (название столбца, *может быть null, *главный ключ)

# UPD 16.10: во write больше не надо подовать массив, просто все значения которые нужны
