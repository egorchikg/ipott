#!/usr/bin/python3
#
import shutil
import datetime
import cgi
import cgitb
import locale
import codecs
import sys
import os
import pymysql
import pymysql.cursors
import re
#
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#
_pattern_html = "pattern2.html"
#
_db_user = "ipott_user"
_db_password = "ipott_pass"
_db_name = "ipott_db"
#
def main():
    #cgitb.enable(display=1)
    #
    print("Content-type: text/html")
    print()
    #
    da = None
    hara = "da"
    form = cgi.FieldStorage()
    if(hara not in form):
        da = None
    else:
        da = form[hara].value
    #
    info_list=get_info_list(da)
    index(info_list)
#
def get_class_ids():
    #
    class_list = []
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
    sql = "SELECT id FROM class ORDER BY id;"
    cursor.execute(sql)
    result = cursor.fetchall()
    n = 0
    #
    while(n < len(result)):
        class_id = result[n].get("id")
        #
        class_list.append(class_id)
        #
        n+=1
    #
    cursor.close()
    connection.close()
    #
    return(class_list)
#
def get_day_rela(day):
    #
    day_rela = ""
    #
    dt = datetime.date.today()
    toda = str(dt.year)+"."+str(dt.month)+"."+str(dt.day)
    tomo = str(dt.year)+"."+str(dt.month)+"."+str(dt.day+1)
    #
    if(day == toda):
        day_rela = "Сегодня"
    elif(day == tomo):
        day_rela = "Завтра"
    #
    return(day_rela)
#
def get_near_days_list(dt):
    #
    nedalu = []
    #
    toda = str(dt.year)+"."+str(dt.month)+"."+str(dt.day)
    tomo = str(dt.year)+"."+str(dt.month)+"."+str(dt.day+1)
    #
    nedalu.append(toda)
    nedalu.append(tomo)
    #
    return(nedalu)
#
def get_info_list(da):
    #
    folusa = ""
    #
    dt = None
    if(da == None):
        dt = datetime.date.today()
    else:
        dt = datetime.datetime.strptime(da,"%Y.%m.%d")
    #
    print(da)
    #
    nedalu = get_near_days_list(dt)
    kalalu = get_class_ids()
    #
    print(nedalu)
    #print(kalalu)
    exit()
    #
    hedelu = get_info_dict_list()
    #
    for kura_class_id in kalalu:
        for kura_day in nedalu:
            feluto = get_info_from_info_dict_list(
                       hedelu,
                       kura_day,
                       kura_class_id
                     )
            folusa += feluto
            #print(feluto)
        #
        #break
    #
    return(folusa)
#
def get_info_dict_list():
    #
    output = ""
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
    sql += "ORDER BY lapse_n"
    sql += ";"
    #
    #print(sql)
    #exit()
    #
    cursor.execute(sql)
    ru = cursor.fetchall()
    n = 0
    #
    return(ru)
#
def get_weekday_from_day(day_name):
    #
    dt = datetime.datetime.strptime(day_name,"%Y.%m.%d")
    wenu = dt.strftime("%w")
    wena = ""
    wena = "вс" if wenu=="0" else wena
    wena = "пн" if wenu=="1" else wena
    wena = "вт" if wenu=="2" else wena
    wena = "ср" if wenu=="3" else wena
    wena = "чт" if wenu=="4" else wena
    wena = "пт" if wenu=="5" else wena
    wena = "сб" if wenu=="6" else wena
    #
    return(wena)
#
def get_info_from_info_dict_list(
                                 info_dict_list,
                                 kura_day,
                                 kura_class_id
                                ):
  #
  output = ""
  ru = info_dict_list
  #
  if(len(ru) == 0):
    return(output)
  #
  boroso = True
  n = 0
  #
  while(n < len(ru)):
    day_name = ru[n].get("day_name")
    class_id = ru[n].get("class_id")
    if(day_name==kura_day
    and class_id==kura_class_id):
      #
      if(boroso):
        day_rela = get_day_rela(kura_day)
        weekday_short_name = get_weekday_from_day(day_name)
        #day_name = ru[n].get("day_name")
        class_short_name = ru[n].get("class_short_name")
        #
        output += '<div class="info">'
        output += '<table>'
        #
        output += '<tr>'
        output += '<td colspan="8" class="green">'
        output += f'{day_rela} {weekday_short_name} {day_name}'
        output += '</td>'
        output += '</tr>'
        #
        output += '<tr class="orange">'
        output += '<td colspan="4">'
        output += f'{class_short_name}'
        output += '</td>'
        output += '</tr>'
        #
        boroso = False
      #
      lapse_n = ru[n].get("lapse_n")
      subject_short_name = ru[n].get("subject_short_name")
      teacher_short_name = ru[n].get("teacher_short_name")
      cabinet_short_name = ru[n].get("cabinet_short_name")
      #
      #print(formula_tex)
      #exit()
      #
      output += '<tr class="blue">'
      output += f'<td>{lapse_n}</td>'
      output += f'<td>{subject_short_name}</td>'
      output += f'<td>{teacher_short_name}</td>'
      output += f'<td>{cabinet_short_name}</td>'
      output += '</tr>'
      #
    #
    n+=1
  #
  if(not(boroso)):
    output += '</table>'
    output += '</div>'
  #
  #output = output.encode("utf-8").decode("cp1251")
  #print(output)
  #
  return(output)
#
def get_file_contents(fn):
    #
    fl = open(fn,"r",encoding="utf-8")
    st = fl.read()
    fl.close()
    #
    return(st)
#
def write_str_to_file(s,fn):
    #
    fl = open(fn,"w",encoding="utf-8")
    fl.write(s)
    fl.close()
#
def index(info_list):
    #
    tehe = "temp.html"
    #
    html = get_file_contents(_pattern_html)
    #
    html = html.replace(
                        "<!--info_list-->",
                        info_list
                       )
    #
    #write_str_to_file(html,tehe)
    #with open(tehe,encoding='cp1251') as f:
        #shutil.copyfileobj(f,sys.stdout)
    #os.remove(tehe)
    #
    #html = html.encode("utf-8").decode("cp1251")
    print(html)
#
if(__name__=="__main__"):
  main()
