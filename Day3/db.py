import sqlite3

def createDBAndTable():
    conn = sqlite3.connect('trainings.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE training
                (id int, name text, duration text)''')
    c.execute("INSERT INTO training VALUES(1,'Docker','3 days')")
    c.execute("INSERT INTO training VALUES(3,'DevOps','5 days')" )

    conn.commit()
    conn.close()

def readFromDB():
    conn = sqlite3.connect('trainings.db')
    c = conn.cursor()
    c.execute('''SELECT * FrOM training''')

    print ( c.fetchall() )

    c.close()


if __name__ == "__main__":
    createDBAndTable()
    readFromDB()