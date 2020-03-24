# liberias de panda
import pandas as pd 

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Cobartram016\TRABDSP10;'
                      'Database=BDVIAJE2;'
                      'UID=tra-sap;'
                      'PWD=12345.TS;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()

cursor.execute("SELECT * FROM DC_Usuarios Where correo='prueba@trasenlca.com'")
for row in cursor:
    print(row)

