import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insertVariableIntoTable(machine, value, send_date):
    try:
        sqliteConnection = sqlite3.connect("arduino.db")
        cursor = sqliteConnection.cursor()
        print("Connected...")
        sqlite_insert_with_param = """INSERT INTO kullanim (
                            id, machine, value, send_date)
                            VALUES (NULL, ?, ?, ?);"""

        data_tuple = (machine, value, send_date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python variables inserted sccessfully into to table")

        cursor.close()

    except Error:
        print("Failed to insert Python variable into sqlite table", Error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQL connection is closed...")


def main():
    database = r"arduino.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS kullanim (
                                        id integer PRIMARY KEY,
                                        machine text NOT NULL,
                                        value text NOT NULL,
                                        send_date text NOT NULL); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
