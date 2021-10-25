#!/usr/bin/python3
#
import sys
import json
import datetime
import pymysql
import pymysql.cursors
import os
#
_db_user = "ipott_user"
_db_password = "ipott_pass"
_db_name = "ipott_db"
_pattern = "lesson.html"
#
def menene():
    #
    reqmet = os.environ["REQUEST_METHOD"]
    #reqmet = "GET"
    if(reqmet == "GET"):
        get()
    elif(reqmet == "POST"):
        post()
    else:
        print("Content-type: text/html;charset=utf-8")
        print()
        print("error")
    #
#
def get():
    #
    print("Content-type: text/html;charset=utf-8")
    print()
    lakebo = get_file_contents(_pattern)
    #
    lavero = get_insert_block()
    denede = get_delete_block()
    benede = get_datalists()
    #
    lakebo = lakebo.replace(
            "<!--datalists-->",
            benede
        )
    #
    lakebo = lakebo.replace(
            "<!--insert_block-->",
            lavero
        )
    #
    lakebo = lakebo.replace(
            "<!--delete_block-->",
            denede
        )
    #
    print(lakebo)
    #
#
def post():
    #
    print("Content-type: text/html;charset=utf-8")
    print()
    #
    resope = json.load(sys.stdin)
    '''
    resope = {
        "command": "insert",
        "lesson_id": "0",
        "day_id": "1",
        "weekday_id": "1",
        "lapse_id": "1",
        "subject_id": "1",
        "cabinet_id": "1",
        "teacher_id": "1",
        "class_id": "1",
    }
    '''
    #
    #
    if(resope["command"] == "insert"):
        valusa = get_insert_valusa(resope)
        insert_into_lesson(valusa)
        print("inserting done!")
    elif(resope["command"] == "delete"):
        valusa = get_delete_valusa(resope)
        delete_from_lesson(valusa)
        print("deleting done!")
    else:
        print(resope["command"])
    #
#
def insert_into_lesson(valusa):
    #
    connection = pymysql.connect(host='localhost',
        user=_db_user,
        password=_db_password,
        database=_db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    #
    cursor = connection.cursor()
    #
    sql = f"INSERT INTO lesson VALUES ({valusa});"
    cursor.execute(sql)
    #
    connection.commit()
    #
    cursor.close()
    connection.close()
    #
#
def delete_from_lesson(valusa):
    #
    connection = pymysql.connect(host='localhost',
        user=_db_user,
        password=_db_password,
        database=_db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    #
    cursor = connection.cursor()
    #
    sql = f"DELETE FROM lesson WHERE {valusa};"
    cursor.execute(sql)
    #
    connection.commit()
    #
    cursor.close()
    connection.close()
    #
#
def get_delete_valusa(resope):
    #
    valusa = ""
    valusa += 'day_id="'+resope["day_id"]+'" AND '
    valusa += 'weekday_id="'+resope["weekday_id"]+'" AND '
    valusa += 'lapse_id="'+resope["lapse_id"]+'" AND '
    valusa += 'subject_id="'+resope["subject_id"]+'" AND '
    valusa += 'cabinet_id="'+resope["cabinet_id"]+'" AND '
    valusa += 'teacher_id="'+resope["teacher_id"]+'" AND '
    valusa += 'class_id="'+resope["class_id"]+'"'
    #
    return(valusa)
#
def get_insert_valusa(resope):
    #
    valusa = ""
    valusa += '"'+resope["lesson_id"]+'",'
    valusa += '"'+resope["day_id"]+'",'
    valusa += '"'+resope["weekday_id"]+'",'
    valusa += '"'+resope["lapse_id"]+'",'
    valusa += '"'+resope["subject_id"]+'",'
    valusa += '"'+resope["cabinet_id"]+'",'
    valusa += '"'+resope["teacher_id"]+'",'
    valusa += '"'+resope["class_id"]+'"'
    #
    return(valusa)
#
def get_dict_from_table(tname):
    #
    connection = pymysql.connect(host='localhost',
        user=_db_user,
        password=_db_password,
        database=_db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    #
    cursor = connection.cursor()
    #
    sql = f"SELECT * FROM {tname};"
    cursor.execute(sql)
    result = cursor.fetchall()
    #
    cursor.close()
    connection.close()
    #
    return(result)
    #
#
def get_day_datalist():
    #
    tname = "day"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rnm = rova["name"]
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_search_input(tname,phold,cla,disabled=False):
    #
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}" '
    leseke += 'disabled' if disabled else ''
    leseke += '>'
    #
    return(leseke)
#
def get_weekday_datalist():
    #
    tname = "weekday"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rn = rova["n"]
        rnm = rova["short_name"]
        leseke += f'<option data-id="{rid}" '
        leseke += f'data-n="{rn}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_class_datalist():
    #
    tname = "class"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rnm = rova["short_name"]
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_lapse_datalist():
    #
    tname = "lapse"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rnm = rova["n"]
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_subject_datalist():
    #
    tname = "subject"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rnm = rova["short_name"]
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_teacher_datalist():
    #
    tname = "teacher"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rnm = rova["short_name"]
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_cabinet_datalist():
    #
    tname = "cabinet"
    tdict = get_dict_from_table(tname)
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    for rova in tdict:
        rid = rova["id"]
        rnm = rova["short_name"]
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    leseke += '</datalist>'
    #
    return(leseke)
#
def get_datalists():
    #
    lesene = ""
    lesene += get_day_datalist()
    lesene += get_weekday_datalist()
    lesene += get_class_datalist()
    lesene += get_lapse_datalist()
    lesene += get_subject_datalist()
    lesene += get_teacher_datalist()
    lesene += get_cabinet_datalist()
    #
    return(lesene)
#
def get_button(title,cla):
    #
    le = ""
    le += f'<button class="{cla}">{title}</button>'
    #
    return(le)
#
def get_insert_block():
    #
    cla = "insert"
    #
    le = ""
    le += get_search_input("day","дата",cla)
    le += get_search_input("weekday","день недели",cla,True)
    le += get_search_input("class","класс",cla)
    le += get_search_input("lapse","номер урока",cla)
    le += get_search_input("subject","предмет",cla)
    le += get_search_input("teacher","учитель",cla)
    le += get_search_input("cabinet","кабинет",cla)
    le += get_button("Добавить",cla)
    #
    return(le)
#
def get_delete_block():
    #
    cla = "delete"
    #
    le = ""
    le += get_search_input("day","дата",cla)
    le += get_search_input("weekday","день недели",cla,True)
    le += get_search_input("class","класс",cla)
    le += get_search_input("lapse","номер урока",cla)
    le += get_search_input("subject","предмет",cla)
    le += get_search_input("teacher","учитель",cla)
    le += get_search_input("cabinet","кабинет",cla)
    le += get_button("Удалить&nbsp;",cla)
    #
    return(le)
#
def get_file_contents(fn):
    #
    fl = open(fn,"r",encoding="utf-8")
    st = fl.read()
    fl.close()
    #
    return(st)
#
if(__name__=="__main__"):
    menene()
