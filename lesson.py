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
    valusa = get_valusa(resope)
    insert_into_lesson(valusa)
    #
    print("yea!")
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
def get_valusa(resope):
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
def get_day_search_input():
    #
    tname = "day"
    phold = "дата"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}">'
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
def get_weekday_search_input():
    #
    tname = "weekday"
    phold = "день недели"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}" disabled>'
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
def get_class_search_input():
    #
    tname = "class"
    phold = "класс"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}">'
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
def get_lapse_search_input():
    #
    tname = "lapse"
    phold = "номер урока"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}">'
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
def get_subject_search_input():
    #
    tname = "subject"
    phold = "предмет"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}">'
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
def get_teacher_search_input():
    #
    tname = "teacher"
    phold = "учитель"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}">'
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
def get_cabinet_search_input():
    #
    tname = "cabinet"
    phold = "кабинет"
    cla = "insert"
    leseke = ""
    leseke += f'<input type="search" list="{tname}" '
    leseke += f'placeholder="{phold}" class="{cla}">'
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
def get_insert_block():
    #
    lesene = ""
    lesene += get_day_search_input()
    lesene += get_weekday_search_input()
    lesene += get_class_search_input()
    lesene += get_lapse_search_input()
    lesene += get_subject_search_input()
    lesene += get_teacher_search_input()
    lesene += get_cabinet_search_input()
    lesene += '<button class="insert">Добавить</button>'
    #
    return(lesene)
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
