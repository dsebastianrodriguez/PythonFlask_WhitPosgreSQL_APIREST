from database.db import get_connection
from .entities.Employed import Employed

class EmployedModel():
    @classmethod
    def get_employed(self):
        try:
            connection=get_connection()
            employed=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, charge, salary, startdate FROM employedbd ORDER BY name ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    employ=Employed(row[0],row[1],row[2],row[3],row[4])
                    employed.append(employ.to_JSON())

            connection.close()
            return employed
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_employ(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, charge, salary, startdate FROM employedbd WHERE id = %s",(id,))
                row=cursor.fetchone()
                employ=None
                if row != None:
                    employ=Employed(row[0],row[1],row[2],row[3],row[4])
                    employ=employ.to_JSON()

            connection.close()
            return employ
        except Exception as ex:
            raise Exception(ex)


    
    @classmethod
    def add_employ(self,employe):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO employedbd (id, name, charge, salary,startdate) VALUES (%s, %s, %s, %s, %s)",(employe.id,employe.name,employe.charge,employe.salary,employe.startdate))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_employ(self,employe):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE employedbd SET name=%s, charge=%s, salary=%s, startdate=%s WHERE id=%s",(employe.name,employe.charge,employe.salary,employe.startdate,employe.id))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_employ(self,employe):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM employedbd WHERE id=%s", (employe.id,))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)