#BackEnd

import sqlite3

def studentData():
    con = sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdId text, Firstname text,\
                  Surname text, DoB text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def addStdRec(StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES(NULL, ?,?,?,?,?,?,?,?)",(StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE ID=?", (id,))
    con.commit()
    con.close()

def searchData(StdId="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdId=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? \
                OR Gender=? OR Address=? OR Mobile=?",(StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,StdId="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdId=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?,\
                 Address=?,Mobile=?, WHERE id=?",(StdId, Firstname, Surname, DoB, Age, Gender, Address, Mobile,id))
    con.commit()
    con.close()

    


