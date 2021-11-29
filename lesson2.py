#!/usr/bin/python3
#
import sys
import json
import datetime
import pymysql
import pymysql.cursors
import os
import time
#
_db_user = "ipott_user"
_db_password = "ipott_pass"
_db_name = "ipott_db"
_pattern = "lesson2.html"
#
def menene():
    #
    add_new_dates()
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
    '''
    lakebo = lakebo.replace(
            "<!--delete_block-->",
            denede
        )
    '''
    #
    print(lakebo)
    #
#
def post():
    #
    #print("Content-type: text/html;charset=utf-8")
    print("Content-Type: application/json;charset=utf-8")
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
        re = insert_into_lesson(valusa)
        print(re)
    elif(resope["command"] == "update"):
        valusa = get_update_valusa(resope)
        re = update_lesson(valusa,resope["lesson_id"])
        print(re)
    elif(resope["command"] == "delete"):
        valusa = get_delete_valusa(resope)
        re = delete_from_lesson(valusa)
        print(re)
    else:
        print(resope["command"])
    #
#
def add_new_dates():
    #
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
    dale = get_near_days(7)
    #print(f"<script>console.log('{dale}');</script>")
    #
    for he in dale:
        try:
            sql = f'INSERT INTO day VALUES (0,"{he}");'
            cursor.execute(sql)
        except Exception as ke:
            #print(ke)
            time.sleep(0)
    #
    connection.commit()
    #
    cursor.close()
    connection.close()
    #
#
def get_near_days(nu):
    #
    re = []
    #
    dt = datetime.date.today()
    dts = dt.strftime("%Y.%m.%d")
    re.append(dts)
    #
    for i in range(nu):
        dt += datetime.timedelta(days=1)
        dts = dt.strftime("%Y.%m.%d")
        re.append(dts)
    #
    return(re)
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
    sql += "lesson.id AS lesson_id, "
    sql += "lesson.day_id AS day_id, "
    sql += "lesson.class_id AS class_id, "
    sql += "lesson.lapse_id AS lapse_id, "
    sql += "lesson.subject_id AS subject_id, "
    sql += "lesson.teacher_id AS teacher_id, "
    sql += "lesson.cabinet_id AS cabinet_id, "
    #
    sql += "day.name AS day_name, "
    sql += "class.short_name AS class_name, "
    sql += "lapse.n AS lapse_name, "
    sql += "subject.short_name AS subject_name, "
    sql += "teacher.short_name AS teacher_name, "
    sql += "cabinet.short_name AS cabinet_name "
    #
    sql += "FROM "
    sql += "lesson,day,class,lapse,subject,teacher,cabinet "
    sql += "WHERE "
    sql += "lesson.day_id = day.id AND "
    sql += "lesson.class_id = class.id AND "
    sql += "lesson.lapse_id = lapse.id AND "
    sql += "lesson.subject_id = subject.id AND "
    sql += "lesson.teacher_id = teacher.id AND "
    sql += "lesson.cabinet_id = cabinet.id "
    sql += "ORDER BY lapse.n"
    sql += ";"
    #
    #print(sql)
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
    #print("filter")
    #
    if(len(ru) == 0):
      print("lo")
      return(hotu)
    #
    n = 0
    del re["command"]
    #
    #print(len(ru))
    #print(set(re.keys()))
    #
    while(n < len(ru)):
        ka = 0
        for ve in set(re.keys()):
            #
            if(str(ru[n][ve]) == str(re[ve])):
                ka+=1
            #
        #
        if(ka == len(re.keys())):
            hotu.append(ru[n])
        #
        n+=1
    #
    return(hotu)
    #
#
def select_from_lesson(resope):
    #
    hedelu = get_info_dict_list()
    #
    fedelu = filter_dict_list(hedelu,resope)
    for he in fedelu:
        he["command"] = "append"
    #
    #print(fedelu)
    #print()
    #print("sele")
    #print()
    #
    re = json.dumps(fedelu)
    #
    return(re)
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
    rule = []
    ru = {}
    ru["command"] = "alert"
    ru["message"] = "inserting done!"
    rule.append(ru)
    re = json.dumps(rule)
    return(re)
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
    rule = []
    ru = {}
    ru["command"] = "alert"
    ru["message"] = "updating done!"
    rule.append(ru)
    re = json.dumps(rule)
    return(re)
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
    rule = []
    ru = {}
    ru["command"] = "alert"
    ru["message"] = "deleting done!"
    rule.append(ru)
    re = json.dumps(rule)
    return(re)
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
def get_options(tname):
    #
    tdict = get_dict_from_table(tname)
    leseke = ""
    for rova in tdict:
        rid = rova["id"]
        rnm = ""
        #
        if(False):
            rnm = ""
        elif(tname=="day"):
            rnm = rova["name"]
        elif(tname=="lapse"):
            rnm = rova["n"]
        elif(True):
            rnm = rova["short_name"]
        #
        leseke += f'<option data-id="{rid}">{rnm}</option>'
    #
    return(leseke)
    #
#
def get_datalist(tname):
    #
    leseke = ""
    leseke += f'<datalist id="{tname}">'
    leseke += get_options(tname);
    leseke += '</datalist>'
    #
    return(leseke)
    #
#
def get_datalists():
    #
    tnames = [
        "day",
        "class",
        "lapse",
        "subject",
        "teacher",
        "cabinet"
    ]
    #
    lesene = ""
    for tname in tnames:
        lesene += get_datalist(tname)
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
def get_select(hopote,kale):
    #
    kalese = " ".join(kale)
    le = ""
    le += f'<select class="{kalese}">'
    le += hopote
    le += '</select>'
    #
    return(le)
#
def get_date_input(kale):
    #
    kalese = " ".join(kale)
    le = ""
    le += f'<input type="date" class="{kalese}">'
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
    #
    kale = list(clali)
    kale.insert(0,"day")
    le += get_date_input(kale)
    #
    tnames = [
        "class",
        "lapse",
        "subject",
        "teacher",
        "cabinet"
    ]
    #
    lesene = ""
    for tname in tnames:
        kale = list(clali)
        kale.insert(0,tname)
        hopote = get_options(kale[0])
        le += get_select(hopote,kale)
    #
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
