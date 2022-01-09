import psycopg2
from datetime import datetime, date, time
start = date(2021, 9, 1)
conn = psycopg2.connect(database="rasp",
                        user="postgres",
                        password="1304",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


def answ_bd(day, next = 0):
    if next == 0:
        week = datetime.now().isocalendar()[1] - start.isocalendar()[1] + 1
    else:
        week = datetime.now().isocalendar()[1] - start.isocalendar()[1] + 2
    mig = (week+1) % 2 + 1
    select_query_day = f"""Select * from timetable where day={day} and mig in ({mig}, 0) order by start_time"""
    cursor.execute(select_query_day)
    records = cursor.fetchall()
    L1 = ""
    L2 = ""
    L3 = ""
    L4 = ""
    L5 = ""
    for row in records:
        if str(row[5]) == "09:30:00":
            L1 = str(row[3])
        if str(row[5]) == "11:20:00":
            L2 = str(row[3])
        if str(row[5]) == "13:10:00":
            L3 = str(row[3])
        if str(row[5]) == "15:25:00":
            L4 = str(row[3])
        if str(row[5]) == "17:15:00":
            L5 = str(row[3])
    if L1 == "":
        L1 = "Отсутсвует"
    if L2 == "":
        L2 = "Отсутсвует"
    if L3 == "":
        L3 = "Отсутсвует"
    if L4 == "":
        L4 = "Отсутсвует"
    if L5 == "":
        L5 = "Отсутсвует"

    result = f"Первая пара: {L1}\n" \
             f"Вторая пара: {L2}\n" \
             f"Третья пара: {L3}\n" \
             f"Четвёртая пара: {L4}\n" \
             f"Пятая пара: {L5}\n"
    return (result)


def Wansw_bd(next):
    if next == 0:
        week = "эту"
    else:
        week = "следующую"
    result = f"Расписание на {week} неделю:\n" \
             f"⭐️Понедельник:\n" \
             f"{answ_bd(1, next)}" \
             f"⭐️Вторник:\n" \
             f"{answ_bd(2,next)}" \
             f"⭐️Среда:\n" \
             f"{answ_bd(3,next)}" \
             f"⭐️Четверг:\n" \
             f"{answ_bd(4, next)}" \
             f"⭐️Пятница:\n" \
             f"{answ_bd(5, next)}" \
             f"⭐️Суббота:\n" \
             f"{answ_bd(6, next)}"
    return (result)


def week_bd():
    week = datetime.now().isocalendar()[1] - start.isocalendar()[1] + 1
    mig = (week + 1) % 2 + 1
    if mig == 1:
        result = "Сейчас верхняя неделя"
    elif mig == 2:
        result = "Сейчас нижняя неделя"
    return (result)
