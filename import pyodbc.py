import pyodbc
import csv

connection = pyodbc.connect("Driver={SQL Server};"
                      "Server=Cobartram016\TRABDSP10;"
                      "Database=BDVIAJE2;"
                      "uid=tra-sap;pwd=12345.TS")

cursor = connection.cursor()

cursor.execute("SELECT * FROM DC_Usuarios")
data=cursor.fetchall()

with open('dataTester.csv', 'w', newline='') as fp:
    a= csv.writer(fp, delimiter=',')
    for line in data:
        a.writerows(line)

for row in data:
    print (row[0],row[1],row[2])
cursor.close()
connection.close()










;;;;;;;;;;;;;;;;;;;
# Client Automation Script
import pyodbc
import csv
cnxn = pyodbc.connect('Driver={SQL Server};Server=Cobartram016\TRABDSP10;DATABASE=BDVIAJE2;UID=tra-sap;PWD=12345.TS')
with open('maqueta.csv') as csvfile:
        data = csv.reader(csvfile)
        cursor = cnxn.cursor()
        for row in data:
            cursor.execute('INSERT INTO BDVIAJE2.dbo.DC_Usuarios(correo,id_company,nombres,apellidos,extension,celular,puesto,pagina_web,ciudad,departamento,area,pais,codigo_postal) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
            Print("Done")
            cursor.close()
            cnxn.commit()