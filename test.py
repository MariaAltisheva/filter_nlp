import sqlite3
from lists import list_city, list_type_auto, list_type_cargo, list_payment, valuta
import datetime

start_time = datetime.datetime.now()

# Подключение к базе данных
conn = sqlite3.connect('database_site.db')

# Создание объекта-курсора
cur = conn.cursor()

# Выполнение запроса
cur.execute("SELECT text FROM message_2")
count = 1
# Обработка результатов
dict_ = {}
list_ = []
# while True:
for row in cur:
    # print(row)
    dict_[count] = {}
    string = ''.join(row)
    string = string.lower()
    city_list_detect = string.split(' ' or '-')
    # print(city_list_detect)
    for c in city_list_detect:
        # print(c.lower())
        for c2 in list_city:
            if c.find(c2) >= 0:
                # print(c2, c)
                dict_[count]['departure_city'] = c2
                break
            else:
                dict_[count]['departure_city'] = None
        if dict_[count]['departure_city']:
            break

    for i in list_type_auto:
        if i in string:
            dict_[count]['type_auto'] = i
            break
        else:
            dict_[count]['type_auto'] = None

    for j in list_type_cargo:
        if j in string:
            dict_[count]['type_cargo'] = j
            break
        else:
            dict_[count]['type_cargo'] = None
    for k in list_payment:
        if k in string:
            dict_[count]['premayment'] = k
            break
        else:
            dict_[count]['premayment'] = None
    for p in valuta:
        if p in string:
            dict_[count]['currency'] = p
            break
        else:
            dict_[count]['currency'] = None

    values_list = tuple(dict_[count].values())
    list_.append(values_list)
    count += 1

print(list_)


# Закрытие соединения с базой данных
conn.commit()
conn.close()

finish_time = datetime.datetime.now()

print(finish_time - start_time)