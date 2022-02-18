import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create database connection
    :param db_file: database file
    :return: Connection object
    """
    conn = None 
    try:
        conn = sqlite3.connect(db_file)
        print("Successful Connected!")
    except Error as e:
        print(e)

    return conn 

def create_table(conn, person):
    """ create database table
    :param conn: db conn
    :return: table
    """
    # sql1 = """ CREATE TABLE dev(name TEXT,address TEXT,total_viz INTEGER,follower INTEGER,following INTEGER,url TEXT) """
    # cursor = conn.cursor()
    sql = ''' INSERT INTO dev(name,address,total_viz,follower,following,url) VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    print("Cursor success!")
    # cur.execute(sql1)
    # conn.commit()
    cur.execute(sql, person)
    conn.commit()
    return cur.lastrowid

# database = 'test.db'
# conn = create_connection(database)
# with conn:
#     data = ("test","test",1,1,2,"www")
#     create_table(conn,data)