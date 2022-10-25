import dbinfo as db

class SungJukV8DAO:
    @staticmethod
    def insert_sungjuk(sj):
        conn, cur = db.openConn()
        sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) values (%s, %s, %s, %s, %s, %s, %s)'

        params = [sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd]
        cur.execute(sql, params)
        cnt = cur.rowcount
        conn.commit()

        db.closeConn(cur, conn)

        return cnt

    @staticmethod
    def select_sungjuk():
        # 성적테이블에서 이름/국어/영어/수학만 select해서 출력
        conn, cur = db.openConn()

        sql = 'select name, tot, grd from sungjuk order by sjno'
        cur.execute(sql)
        rows = cur.fetchall()

        db.closeConn(conn, cur)

        return rows

    @staticmethod
    def select_one_sungjuk(name):
        # 입력한 학생이름으로 설적테이블을 조회해서 조회된 결과를 출력
        conn, cur = db.openConn()

        sql = 'select * from sungjuk where name = %s'
        cur.execute(sql, [name])
        row = cur.fetchone()

        db.closeConn(conn, cur)

        return row

    @staticmethod
    def update_sungjuk(sj):
        conn, cur = db.openConn()
        sql = 'update sungjuk set kor=%(kr)s, eng=%(en)s, mat=%(mt)s, tot=%(tt)s, avg=%(av)s, grd=%(gd)s where name = %(nm)s'
        params = dict(nm=sj.name, kr=sj.kor, en=sj.eng, mt=sj.mat, tt=sj.tot, av=sj.avg, gd=sj.grd)
        cur.execute(sql, params)
        cnt = cur.rowcount
        conn.commit()

        db.closeConn(cur,conn)

        return cnt

    @staticmethod
    def delete_sungjuk(name):
        conn, cur = db.openConn()

        sql = 'delete from sungjuk where name = %s'
        cur.execute(sql, [name])
        cnt = cur.rowcount
        conn.commit()

        db.closeConn(conn, cur)

        return cnt