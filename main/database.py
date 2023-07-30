import sqlite3
from internet import internet_conn


def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection


def insert_qsn_ans(qsn, ans):
    conn = create_connection()
    cur = conn.cursor()
    query = "INSERT INTO question_answers values('" + qsn + "','" + ans + "')"
    cur.execute(query)
    conn.commit()


def get_qsn_ans():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(" SELECT * FROM question_answers")
    return cur.fetchall()


def get_ans(ques):
    rows = get_qsn_ans()
    ans = ""
    for row in rows:
        if (row[0].lower()) in ques.lower():
            ans = row[1]
            break
    return ans


def get_name():
    conn = create_connection()
    cur = conn.cursor()
    query = "select value from mem where name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(new_name):
    conn = create_connection()
    cur = conn.cursor()
    query = "update mem set value='" + new_name + "'where name = 'assistant_name'"
    cur.execute(query)
    conn.commit()


def update_prev_date(prev_date):
    conn = create_connection()
    cur = conn.cursor()
    query = "update mem set value='" + str(prev_date) + "'where name = 'prev_date'"
    cur.execute(query)
    conn.commit()


def get_prev_date():
    conn = create_connection()
    cur = conn.cursor()
    query = "select value from mem where name = 'prev_date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])


def speak_on():
    if (internet_conn):
        conn = create_connection()
        cur = conn.cursor()
        query = "update mem set value='on' where name = 'speak'"
        cur.execute(query)
        conn.commit()
        return "Speak turned on"
    else:
        return "Sir please enable your internet"


def speak_off():
    conn = create_connection()
    cur = conn.cursor()
    query = "update mem set value='off' where name = 'speak'"
    cur.execute(query)
    conn.commit()
    return "Speak turned off"


def speak_is_on():
    conn = create_connection()
    cur = conn.cursor()
    query = "select value from mem where name = 'speak'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    else:
        return False

def speech_on():
    if (internet_conn):
        conn = create_connection()
        cur = conn.cursor()
        query = "update mem set value='on' where name = 'speech'"
        cur.execute(query)
        conn.commit()
        return "Speech turned on"
    else:
        return "Sir please enable your internet"

def speech_off():
    conn = create_connection()
    cur = conn.cursor()
    query = "update mem set value='off' where name = 'speech'"
    cur.execute(query)
    conn.commit()
    return "Speech turned off"


def speech_is_on():
    conn = create_connection()
    cur = conn.cursor()
    query = "select value from mem where name = 'speech'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    else:
        return False