import sqlite3


def ensure_connection(func):
    """ Декоратор для подключения к СУБД: открывает соединение,
        выполняет переданную функцию и закрывает за собой соединение.
        Потокобезопасно!
    """
    def inner(*args, **kwargs):
        with sqlite3.connect('db/Users.db') as conn:
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res

    return inner

#Создания бази данных с пользователями
@ensure_connection
def init_db(conn, force: bool = False):
    """ Проверить что нужные таблицы существуют, иначе создать их

        Важно: миграции на такие таблицы вы должны производить самостоятельно!

        :param conn: подключение к СУБД
        :param force: явно пересоздать все таблицы
    """
    c = conn.cursor()


    if force:
        c.execute('DROP TABLE IF EXISTS tg_users')

    c.execute('''
        CREATE TABLE IF NOT EXISTS tg_users (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL
        )
    ''')

    # Сохранить изменения
    conn.commit()


@ensure_connection
def add_user(conn, user_id: int):
    """
    Добовляет пользователей в базу данних
    """
    c = conn.cursor()
    c.execute('INSERT INTO tg_users (user_id) VALUES (?)', (user_id,))
    conn.commit()
    

@ensure_connection
def user(conn):
    """
    Выводет id всех пользователей
    """
    c = conn.cursor()
    c.execute("SELECT user_id FROM tg_users ORDER BY id")
    return c.fetchall()

twenty_two = user()
