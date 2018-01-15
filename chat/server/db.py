import pymysql

sql = pymysql.connect(host='10.33.1.6', user='root', passwd='password', port=3306, db='mydb')

def showUsers():
    cursor = sql.cursor()
    query = "select * from Usuario"
    cursor.execute(query)

    for (id, Nombre, Contrasena) in cursor:
        print (id, Nombre, Contrasena)
    
    cursor.close()

def createUser(name, password):
    cursor = sql.cursor()
    query = "insert into Usuario (Nombre, Contrasena) values('%s', '%s')" % (name, password)
    cursor.execute(query)
    sql.commit()
    cursor.close()

def login(name, password):
    cursor = sql.cursor()
    query = "select Contrasena from Usuario where Usuario.Nombre = '%s'" % name
    cursor.execute(query)

    row = cursor.fetchone()

    while row is not None:
        if row[0] == password:
            return True
        else:
            return False

    cursor.close()

def addMessage(user, mensaje):
    cursor = sql.cursor()
    query = "insert into Conversacion (Mensaje, user) values('%s', '%s')" % (mensaje, user)
    cursor.execute(query)
    sql.commit()
    cursor.close()