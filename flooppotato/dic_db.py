import sqlite3

__connection = None


# def get_conne():
#     global __connection
#     if __connection is None:
#         __connection = sqlite3.connect('db/Dic.db')
#         return __connection


def ensure_connection(func):
    """ Декоратор для подключения к СУБД: открывает соединение,
        выполняет переданную функцию и закрывает за собой соединение.
        Потокобезопасно!
    """

    def inner(*args, **kwargs):
        with sqlite3.connect('db/Dic.db') as conn:
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res

    return inner


# Создания бази данных со словами если базы даных нету :З
@ensure_connection
def init_db(conn, force: bool = False):
    # get_conne()
    # c = __connection.cursor()
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS words')

    c.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id          INTEGER PRIMARY KEY,
            word       TEXT NOT NULL,
            tr       TEXT NOT NULL
        )
    ''')


@ensure_connection
def createFirstWord(conn):
    c = conn.cursor()
    c.execute("insert into words values (1, 'word', 'слово')")
    # c.execute("insert into words values (2, 'red', 'червоний')")


@ensure_connection
def searchE(conn, word: str):
    c = conn.cursor()
    c.execute("SELECT tr FROM words WHERE word = ?", (word,))
    (wd,) = c.fetchone()
    return wd


@ensure_connection
def searchU(conn, word: str):
    c = conn.cursor()
    c.execute("SELECT word FROM words WHERE tr = ?", (word,))
    (wd,) = c.fetchone()
    return wd


class Check:
    @ensure_connection
    def eCheck(conn):
        c = conn.cursor()
        c.execute("SELECT word FROM words ORDER BY id")
        return c.fetchall()

    @ensure_connection
    def uCheck(conn):
        c = conn.cursor()
        c.execute("SELECT tr FROM words ORDER BY id")
        return c.fetchall()




# init_db()
# createFirstWord()
