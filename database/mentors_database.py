import sqlite3
import random
from config import bot

def sql_create():
    global mentors_database, cursor
    mentors_database = sqlite3.connect('bot.sqlite3')
    cursor = mentors_database.cursor()

    if mentors_database:
        print("База данных подключена!")

    mentors_database.execute(
        "CREATE TABLE IF NOT EXISTS mentors "
        "(id INTEGER PRIMARY KEY, fullname TEXT, "
        "direction TEXT, age INTEGER, "
        "gruppa TEXT)"
    )
    mentors_database.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        mentors_database.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors ").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id,
                           f"id - {random_user[0]}, \nname - {random_user[1]}, \ndirection - {random_user[2]}, \n"
                           f"age - {random_user[3]}, \ngroup - {random_user[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(mentor_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (int(mentor_id),))
    mentors_database.commit()


async def sql_commands_get_all_id():
    return cursor.execute('SELECT id FROM mentors').fetchall()