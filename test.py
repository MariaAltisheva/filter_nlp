import sqlite3
from lists import list_city, list_type_auto, list_type_cargo, list_payment, valuta, tuple_smile
import datetime
import  re

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
list_spam = []
# while True:
for row in cur:
    # print(row)
    dict_[count] = {}
    # dict_[count]['id'] = count
    dict_[count]['departure_city'] = None
    dict_[count]['destination_city'] = None
    dict_[count]['type_auto'] = None
    dict_[count]['type_cargo'] = None
    dict_[count]['tonnage'] = None
    dict_[count]['stops'] = None
    dict_[count]['prepayment'] = None
    dict_[count]['currency'] = None
    dict_[count]['mode_transportation'] = None
    dict_[count]['type_load'] = None
    dict_[count]['data_load'] = None
    dict_[count]['temperature_regime'] = None
    dict_[count]['cargo_readiness'] = None
    dict_[count]['table_processing'] = None
    dict_[count]['_id'] = None
    dict_[count]['userid'] = None
    dict_[count]['data'] = None
    dict_[count]['phone_num'] = None
    dict_[count]['email'] = None
    dict_[count]['cargo_danger'] = None
    string = ''.join(row)
    string = string.lower()
    city_string = string.replace('-', ' ')
    city_string = city_string.replace('\n', ' ')
    for i in tuple_smile:
        if i in city_string:
            city_string = city_string.replace(i, '')
    # print(city_list_detect)
    city_list_detect = city_string.split()
    # print(city_list_detect)

    for c in city_list_detect:
        for c2 in list_city:
            if c.find(c2) >= 0:
                dict_[count]['departure_city'] = c # можно поставить c2 - будет в более адекватном виде название города
                break
            else:
                dict_[count]['departure_city'] = None
        if dict_[count]['departure_city']:
            break
        # else:
        #     list_spam.append(row)
        #     break
    # try:
    if dict_[count]['departure_city']:
        index_c = city_list_detect.index(dict_[count]['departure_city'])
        # print(index_c)
        for h in range(index_c + 1, len(city_list_detect)):
            for c2 in list_city:
                if city_list_detect[h].find(c2) >= 0:
                    dict_[count]['destination_city'] = city_list_detect[h]
                    break
            if dict_[count]['destination_city']:
                break
    else:
        list_spam.append(row)

    # except:
    #     print('что то не так')
    #     continue


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
        # else:
        #     dict_[count]['type_cargo'] = None
    for k in list_payment:
        if k in string:
            dict_[count]['prepayment'] = k
            break
        # else:
        #     dict_[count]['prepayment'] = None
    for p in valuta:
        if p in string:
            dict_[count]['currency'] = p
            break
        # else:
        #     dict_[count]['currency'] = None

    # фильтр для нахождения номера телефона, состоящего из 9 или 12 цифр
    pattern = r'\d{9,12}'
    match = re.search(pattern, string)
    if match:
        dict_[count]['phone_num'] = match.group()

    if dict_[count]['departure_city'] != None:
        values_list = tuple(dict_[count].values())
        list_.append(values_list)

    # if dict_[count]['departure_city'] == None:
    #     list_spam.append(row)


    count += 1


# print(list_spam)
print(list_)
# print(list_spam)

# Закрытие соединения с базой данных
conn.commit()
conn.close()

finish_time = datetime.datetime.now()

print(finish_time - start_time)