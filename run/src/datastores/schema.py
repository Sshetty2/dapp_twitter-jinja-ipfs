#!/usr/bin/env python3

import sqlite3

CON = None
CUR = None


def setup(dbname="master.db"):
    global CON
    global CUR
    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()

def run():
    SQL = "DROP TABLE IF EXISTS users;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR,
        pass_hash VARCHAR(128),
        type VARCHAR
        );"""
    
    CUR.execute(SQL)
    
    SQL = "DROP TABLE IF EXISTS tweets;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE tweets(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        users_pk INTEGER,
        username VARCHAR,
        content VARHAR,
        image_pathname VARHAR,
        ipfs_hash VARCHAR,
        time INTEGER,
        FOREIGN KEY(users_pk) REFERENCES users(pk),
        FOREIGN KEY(username) REFERENCES users(username)
        );"""
    
    CUR.execute(SQL)

    SQL = "DROP TABLE IF EXISTS users_followed;"

    CUR.execute(SQL)
    
    SQL = """CREATE TABLE users_followed(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        users_pk INTEGER,
        username VARCHAR,
        followed_pk VARCHAR,
        followed_username VARCHAR,
        FOREIGN KEY(users_pk) REFERENCES users(pk),
        FOREIGN KEY(username) REFERENCES users(username),
        FOREIGN KEY(followed_pk) REFERENCES users(pk),
        FOREIGN KEY(followed_username) REFERENCES users(username)
        );"""
    
    CUR.execute(SQL)
    
    CON.commit()
    CUR.close()
    CON.close()

if __name__ == "__main__":
    setup()
    run()
