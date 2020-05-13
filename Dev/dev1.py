import pyodbc

def main():

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=IN2396424W1\SQLEXPRESS;'
                      'Database=eRaptor;'
                      'Trusted_Connection=yes;')
    tnameS = "testcasecreation_dataquality"
    checktableexists(conn, tnameS)

def checktableexists(dbcon, tablename):

    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    exists = dbcur.fetchone()[0]
    if exists == 1:
        print("Exists!")
        dbcur.close()
        return True
    else:
        print("Not Exists!")
    dbcur.close()
    return False

main()