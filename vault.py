import os
import sqlite3


def q(db, term):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM items WHERE name='" + term + "'")
    return cur.fetchall()


def sh(cmd):
    os.system("echo " + cmd)
