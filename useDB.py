#23.08
#упрощение оспользования баз данных, by MaxGyverTech  
import sqlite3

from database import DB

#создать БД
#(название файла, нужен ли вывод к терминал(по умолчанию False))
db = DB('data',debug=True)

#кортеж со столбцами таблици тире их типом данных
tabledict = {
    'name':'TEXT',
    'id':'BIGINT'
    }
#создать таблицу    
#(имя таблицы, кортеж структуры таблицы)
db.createTable(table='users',structure=tabledict)

#проверить еслть ли такая запись в таком то столбце, возвращает false true
#(столбец, значение для поиска)
if db.havewrite('id',str(0)) == False:

    #и записать данные
    #(MАССИВ данных для ваписи,важно что в таком же порядке как и в таблице)
    db.write(['max',0])

#получить всю таблицу, 23.08, метод работает плохо
print(db.getall())

# UPD 25.08: во всех функциях где уместно добавлен НЕОБЯЗАТЕЛЬНЫЙ параметр 'table' для определения таблицы,
# по умолчанию работает с последне таблицой. Теперь необязательные параметры помечаю при помощи "*"

# UPD 25.08: названия аргументов сделаны более интуитивно понятными

# UPD 25.08: добавлен метод изменения записи

db.write(['света',2])         # для проверки
# (значение на которое изменяем, значение по которому ищем какую запись изменить, столбец в котором изменям,*(необязательно)столбец
# покоторому мы можем искать(по умолчанию тот же в который записываем данные),*таблица)
db.edit('egor','max','name')
db.edit(value='катя',idvalue='2',column='name',idcolumn='id',table='users')


# UPD 26.08: добавлена функция удаления записи
db.write(['ivan',10])# для проверки

# просто для прикола и что бы видеть промежуточный результат
if input('Delete?(Y/N)').lower() == 'y':

    # (значение по которому искать, столбец по которому искать, *таблица)
    db.delete('ivan','name')
    # b nen vyt cnfkj ktym gthtrk.xfnm zpsr =)
    db.write(['kto to',666])
    # поодробней ага
    db.delete(idvalue=666,idcolumn='id',table='users')


# 26.08 не понимаю как сделать функцию получения

# всё ещё-.-

# UPD 26.08: ВСЁ, функция поиска сделана

print(db.getline('egor','name'))  # параметры смотрите ниже

# запустите код ещё раз вы создадите вторую катю это важно

# ну что: (значение по которому ищем, столбец по которому ищем,*можно получить не всю строку а конкретный параметр из неё(по умолчанию вся строка),
# *можно ли получить НЕ одну строку(по умолчанию только одну)(ДА ДА функция называется получитьстрокУ но может вернуть несколько строк)),*таблица
a = db.getline(idvalue='катя',idcolumn='name',getval='id',returnone=False,table='users')
print(a)

# тестирую
print(db.getall())

# UPD 26.08: функция получить всё наконец то работает