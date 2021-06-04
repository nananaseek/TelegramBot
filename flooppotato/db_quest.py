import sqlite3
import random


def ensure_connection(func):
    """ Декоратор для подключения к СУБД: открывает соединение,
        выполняет переданную функцию и закрывает за собой соединение.
        Потокобезопасно!
    """

    def inner(*args, **kwargs):
        with sqlite3.connect('db/Quest.db') as conn:
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res

    return inner


# Создания бази данных со словами если базы даных нету :З
@ensure_connection
def init_db(conn, force: bool = False):
    """ Проверить что нужные таблицы существуют, иначе создать их

        Важно: миграции на такие таблицы вы должны производить самостоятельно!

        :param conn: подключение к СУБД
        :param force: явно пересоздать все таблицы
    """
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS quests')

    c.execute('''
        CREATE TABLE IF NOT EXISTS quests (
            id          INTEGER PRIMARY KEY,
            first_q       TEXT NOT NULL,
            second_q       TEXT NOT NULL,
            test        TEXT NOT NULL
        )
    ''')


@ensure_connection
def createfirstWord(conn):
    c = conn.cursor()
    c.execute('''
        insert into quests values(
        1, 
        "lucky you are resting today",
        "lucky you are resting today", 
        "lucky you are resting today"
        )
    ''')


@ensure_connection
def id_quests(conn):
    """
    возвращает последнее id
    """
    c = conn.cursor()
    c.execute("SELECT id FROM quests ORDER BY id DESC limit 0,1")
    (id_numb,) = c.fetchone()
    return id_numb


@ensure_connection
def con_first_q(conn):
    """
    Выводит первый вопрос
    """
    c = conn.cursor()
    c.execute("SELECT first_q FROM quests ORDER BY id")
    return c.fetchall()


@ensure_connection
def con_second_q(conn):
    """
    второй вопрос
    """
    c = conn.cursor()
    c.execute("SELECT second_q FROM quests ORDER BY id")
    return c.fetchall()


@ensure_connection
def con_test_q(conn):
    """
    проверочное слово
    """
    c = conn.cursor()
    c.execute("SELECT test FROM quests ORDER BY id")
    return c.fetchall()


@ensure_connection
def all_id(conn):
    """
    Выводит все id
    *хз зачем*
    """
    c = conn.cursor()
    c.execute("SELECT id FROM quests ORDER BY id")
    a = []

    try:
        for all_id_from_bd in c.fetchall():
            all_id_from_bd = all_id_from_bd[0]
            a.append(all_id_from_bd)
            all_id_from_bd = list(map(int, a))
        return all_id_from_bd
    except UnboundLocalError:
        createfirstWord()


def cool_name_def():
    """
    Адаптирует id  для адекватной работой с id-шками
    """
    rand_con_id = random.randint(1, id_quests())
    rand_con_id = str(rand_con_id - 1)
    return rand_con_id


try:
    random_quest = cool_name_def()
    con_first_q = con_first_q()
    con_second_q = con_second_q()
    con_test_q = con_test_q()
except sqlite3.OperationalError:
    init_db()
    all_id()
    random_quest = cool_name_def()
    con_first_q = con_first_q()
    con_second_q = con_second_q()
    con_test_q = con_test_q()
