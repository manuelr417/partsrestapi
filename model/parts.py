from config.dbconfig import pg_config
import psycopg2

class PartsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" %(pg_config['dbname'], pg_config['user'],
                                                                  pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)
        #self.conn = psycopg2.connect(dbname=pg_config['dbname'],)

    def getAllParts(self):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pweight, pprice from parts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartById(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pweight, pprice from parts where pid = %s;"
        # Bad practice
        #query = "select pid, pname, pmaterial, pcolor, pweight, pprice from parts where pid = " + str(pid)
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def insertPart(self, pname, pcolor, pmaterial, pprice, pweight):
        cursor = self.conn.cursor()
        query = "insert into parts (pname, pcolor, pmaterial, pprice, pweight) values (%s,%s,%s,%s,%s) returning pid;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice, pweight,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def updatePart(self, pid, pname, pcolor, pmaterial, pprice, pweight):
        cursor = self.conn.cursor()
        query= "update parts set pname=%s, pcolor = %s, pmaterial=%s, pprice =%s, pweight=%s where pid=%s;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice, pweight,pid))
        self.conn.commit()
        return True

    def deletePart(self, pid):
        cursor = self.conn.cursor()
        query = "delete from parts where pid=%s;"
        cursor.execute(query,(pid,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows !=0