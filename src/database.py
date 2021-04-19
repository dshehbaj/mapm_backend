import pymysql

def mysqlconnect():
    conn = pymysql.connect(
        host="localhost",
        user="shehbaj",
        password="",
        db="mapm",
        cursorclass=pymysql.cursors.DictCursor
    )
    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output)
    return conn

if __name__ == "__main__":
    mysqlconnect()
