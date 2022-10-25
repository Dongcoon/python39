import pymysql

url = ''
dbid = ''
dbpw = ''
dbname = ''

def openConn():
    conn = pymysql.connect(host=url, user=dbid, password=dbpw, database=dbname, charset='utf8')
    cur = conn.cursor()
    return conn, cur

def closeConn(cur, conn):
    cur.close()
    conn.close()