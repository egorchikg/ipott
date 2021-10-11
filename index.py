#!D:\ilqyul\portpy\python.exe
#
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
_pattern_html = "pattern2.html"
#
_db_user = "lala_user"
_db_password = "lala_pass"
_db_name = "lala_db"
#
def main():
    cgitb.enable(display=1)
    #
    print("Content-type: text/html")
    print()
    #
    info_list=get_info_list()
    index(info_list)
#
def get_menuha():
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
    sql = "SELECT * FROM themes;"
    cursor.execute(sql)
    result = cursor.fetchall()
    n = 0
    #
    output += "<ul>"
    #
    output += '<a href="/">'
    output += '<li>'
    output += get_file_contents("svg/gl.svg")
    output += '</li>'
    output += '</a>'
    #
    while(n < len(result)):
        theme_id = result[n].get("theme_id")
        theme_name = result[n].get("theme_name")
        theme_icon = result[n].get("theme_icon")
        #
        #print(formula_tex)
        #exit()
        #
        output += f'<a href="/?hemado={theme_id}">'
        output += '<li>'
        output += get_file_contents(theme_icon)
        output += '</li>'
        output += '</a>'
        #
        n+=1
    #
    output += "</ul>"
    #
    cursor.close()
    connection.close()
    #
    return(output)
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
    sql = "SELECT id FROM class ORDER BY short_name;"
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
    if(day == toda) {
        day_rela = "Сегодня"
    } elif (day == tomo) {
        day_rela = "Завтра"
    }
    #
    return(day_rela)
#
def get_near_days_list():
    #
    nedalu = []
    #
    dt = datetime.date.today()
    toda = str(dt.year)+"."+str(dt.month)+"."+str(dt.day)
    tomo = str(dt.year)+"."+str(dt.month)+"."+str(dt.day+1)
    #
    nedalu.append(toda)
    nedalu.append(tomo)
    #
    return(nedalu)
#
def get_info_list():
    #
    folusa = ""
    #
    nedalu = get_near_days_list()
    kalalu = get_class_ids()
    #
    for kura_class_id in kalalu:
        for kura_day in nedalu:
            folusa += get_info(kura_day,kura_class_id)
        #
    #
    return(folusa)
#
def get_info(kura_day,kura_class_id):
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
    #sql = "SELECT * FROM lesson;"
    cursor.execute(sql)
    ru = cursor.fetchall()
    n = 0
    #
    day_rela = get_day_rela(kura_day)
    weekday_short_name = ru[n].get("weekday_short_name")
    day_name = ru[n].get("day_name")
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
    while(n < len(ru)):
        interval_n = ru[n].get("interval_n")
        subject_short_name = ru[n].get("subject_short_name")
        teacher_short_name = ru[n].get("teacher_short_name")
        cabinet_short_name = ru[n].get("cabinet_short_name")
        #
        #print(formula_tex)
        #exit()
        #
        output += '<tr class="blue">'
        output += f'<td>{interval_n}</td>'
        output += f'<td>{subject_short_name}</td>'
        output += f'<td>{teacher_short_name}</td>'
        output += f'<td>{cabinet_short_name}</td>'
        output += '</tr>'
        #
        n+=1
    #
    output += '</table>'
    output += '</div>'
    #
    cursor.close()
    connection.close()
    #
    return(output)
#
def get_tanaha(hemado=0):
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
    sql = "SELECT * FROM formulas;"
    cursor.execute(sql)
    result = cursor.fetchall()
    n = 0
    #
    harame = False
    if(hemado == 0):
        harame = True
    #
    while(n < len(result)):
        formula_id = result[n].get("formula_id")
        formula_name = result[n].get("formula_name")
        formula_tex = result[n].get("formula_tex")
        theme_id = result[n].get("theme_id")
        #
        #print(formula_tex)
        #exit()
        #
        if((theme_id == hemado) or harame):
            output += '<div class="t">'
            output += f'{formula_name}'
            output += '</div>'
            output += '<div class="h">'
            output += f'{formula_tex}'
            output += '</div>'
        #
        n+=1
    #
    output = output.encode("utf-8").decode('utf-8')
    #
    cursor.close()
    connection.close()
    #
    return(output)
#
def get_formulas_table():
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
    sql = "SELECT * FROM formulas;"
    cursor.execute(sql)
    result = cursor.fetchall()
    n = 0
    output += "<table>"
    while(n < len(result)):
        formula_id = result[n].get("formula_id")
        formula_name = result[n].get("formula_name")
        formula_tex = result[n].get("formula_tex")
        theme_id = result[n].get("theme_id")
        output += '''<tr>
<td>{formula_id}</td>
<td>{formula_name}</td>
<td>{formula_tex}</td>
<td>{theme_id}</td>
</tr>
'''.format(
           formula_id=formula_id,
           formula_name=formula_name,
           formula_tex=formula_tex,
           theme_id=theme_id
          )
        n+=1
    #
    output += "</table>"
    #
    cursor.close()
    connection.close()
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
def index(info_list):
    #
    html = open(_pattern_html,"r",encoding="utf-8").read()
    #
    html = html.replace(
                        "<!--info_list-->",
                        info_list
                       )
    #
    html = html.encode("utf-8").decode("cp1251")
    #
    print(html)
#
def delete_empty(elements):
    return list(filter(lambda x: x!="",elements))
#
def delete_spaces(elements):
    a = list(elements)
    i = 0
    n = len(a)
    while(i<n):
        a[i]=a[i].strip()
        i+=1
    return(a)
#
if(__name__=="__main__"):
  main()
