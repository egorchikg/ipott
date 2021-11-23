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
    #reqmet = "POST"
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
        "lapse_id": "1",
        "subject_id": "1",
        "cabinet_id": "1",
        "teacher_id": "1",
        "class_id": "1",
    }
    '''
    #
    #
    if(False):
        print()
    elif(resope["command"] == "select"):
        #valusa = get_select_valusa(resope)
        re = select_from_lesson(resope)
        print(re)
    elif(resope["command"] == "insert"):
        valusa = get_insert_valusa(resope)
        insert_into_lesson(valusa)
        print("inserting done!")
    elif(resope["command"] == "update"):
        valusa = get_update_valusa(resope)
        update_lesson(valusa,resope["lesson_id"])
        print("updating done!")
    elif(resope["command"] == "delete"):
        valusa = get_delete_valusa(resope)
        delete_from_lesson(valusa)
        print("deleting done!")
    else:
        print(resope["command"])
    #
#
def get_info_dict_list():
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
    sql = ""
    sql += "SELECT "
    sql += "day.name AS day_name, "
    sql += "class.id AS class_id, "
    sql += "class.short_name AS class_short_name, "
    sql += "lapse.n AS lapse_n, "
    sql += "subject.short_name AS subject_short_name, "
    sql += "teacher.short_name AS teacher_short_name, "
    sql += "cabinet.short_name AS cabinet_short_name "
    sql += "FROM "
    sql += "lesson, day, class, "
    sql += "lapse, subject, teacher, cabinet "
    sql += "WHERE "
    sql += "lesson.day_id = day.id AND "
    sql += "lesson.class_id = class.id AND "
    sql += "lesson.lapse_id = lapse.id AND "
    sql += "lesson.subject_id = subject.id AND "
    sql += "lesson.teacher_id = teacher.id AND "
    sql += "lesson.cabinet_id = cabinet.id "
    #sql += "AND "
    #sql += f"{valusa} "
    sql += "ORDER BY lapse_n"
    sql += ";"
    #
    #lo = f"<script>console.log('{sql}');</script>"
    #print(lo)
    #sql = "SELECT * FROM lesson;"
    #
    cursor.execute(sql)
    ru = cursor.fetchall()
    #print(ru)
    #
    #cursor.close()
    #connection.close()
    #
    return(ru)
    #return(sql)
#
def filter_dict_list(info_dict_list,resope):
    #
    hotu = []
    ru = info_dict_list
    re = resope
    #
    print("filter")
    #
    if(len(ru) == 0):
      print("lo")
      return(hotu)
    #
    n = 0
    del re["command"]
    #
    while(n < len(ru)):
        ka = 0
        for ve in re.keys():
            #
            ka+=1 if ru[n][ve] == re[ve] else ka
            #
        #
        print(ka)
        #
        if(ka == len(re.keys())):
            hotu.append(ru[n])
        #
    #
    return(hotu)
    #
#
def select_from_lesson(resope):
    #
    hedelu = get_info_dict_list()
    #
    fedelu = filter_dict_list(hedelu,resope)
    #
    print(fedelu)
    print()
    print("sele")
    print()
    #
    return(hedelu)
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
def update_lesson(valusa,lesson_id):
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
    sql = f"UPDATE lesson SET {valusa} WHERE id={lesson_id};"
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
def get_select_valusa(resope):
    #
    valusa = None
    z = 0
    va = []
    #
    if("day_id" in set(resope.keys())):
      va.append('lesson.day_id="'+resope["day_id"]+'"')
      z+=1
    if("class_id" in set(resope.keys())):
      va.append('lesson.class_id="'+resope["class_id"]+'"')
      z+=1
    if("lapse_id" in set(resope.keys())):
      va.append('lesson.lapse_id="'+resope["lapse_id"]+'"')
      z+=1
    if("subject_id" in set(resope.keys())):
      va.append('lesson.subject_id="'+resope["subject_id"]+'"')
      z+=1
    if("cabinet_id" in set(resope.keys())):
      va.append('lesson.cabinet_id="'+resope["cabinet_id"]+'"')
      z+=1
    if("teacher_id" in set(resope.keys())):
      va.append('lesson.teacher_id="'+resope["teacher_id"]+'"')
      z+=1
    #
    if(z > 0):
      valusa = " AND ".join(va)
    else:
      valusa = "lesson.id != 0"
    #
    return(valusa)
#
def get_insert_valusa(resope):
    #
    valusa = ""
    valusa += '"'+resope["lesson_id"]+'",'
    valusa += '"'+resope["day_id"]+'",'
    valusa += '"'+resope["lapse_id"]+'",'
    valusa += '"'+resope["subject_id"]+'",'
    valusa += '"'+resope["cabinet_id"]+'",'
    valusa += '"'+resope["teacher_id"]+'",'
    valusa += '"'+resope["class_id"]+'"'
    #
    return(valusa)
#
def get_update_valusa(resope):
    #
    valusa = ""
    valusa += 'day_id="'+resope["day_id"]+'",'
    valusa += 'lapse_id="'+resope["lapse_id"]+'",'
    valusa += 'subject_id="'+resope["subject_id"]+'",'
    valusa += 'cabinet_id="'+resope["cabinet_id"]+'",'
    valusa += 'teacher_id="'+resope["teacher_id"]+'",'
    valusa += 'class_id="'+resope["class_id"]+'"'
    #
    return(valusa)
#
def get_delete_valusa(resope):
    #
    valusa = ""
    valusa += 'id='+resope["lesson_id"]+''
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
def get_hidden_input(value,cla):
    #
    leseke = ""
    leseke += f'<input type="hidden" '
    leseke += f'value="{value}" class="{cla}" '
    leseke += '>'
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
    cla1 = "select"
    cla2 = "insert"
    #
    clali = []
    clali.append(cla1)
    clali.append(cla2)
    #
    clall = " ".join(clali)
    #
    le = ""
    le += get_search_input("day","дата",clall)
    le += get_search_input("class","класс",clall)
    le += get_search_input("lapse","номер урока",clall)
    le += get_search_input("subject","предмет",clall)
    le += get_search_input("teacher","учитель",clall)
    le += get_search_input("cabinet","кабинет",clall)
    le += get_button("Найти",cla1)
    le += get_button("Добавить",cla2)
    #
    return(le)
#
def get_delete_block():
    #
    cla1 = "update"
    cla2 = "delete"
    #
    clali = []
    clali.append(cla1)
    clali.append(cla2)
    #
    clall = " ".join(clali)
    #
    #
    le = ""
    le += get_hidden_input("6",clall)
    le += get_search_input("day","дата",clall)
    le += get_search_input("class","класс",clall)
    le += get_search_input("lapse","номер урока",clall)
    le += get_search_input("subject","предмет",clall)
    le += get_search_input("teacher","учитель",clall)
    le += get_search_input("cabinet","кабинет",clall)
    le += get_button("Изменить",cla1)
    le += get_button("Удалить",cla2)
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
