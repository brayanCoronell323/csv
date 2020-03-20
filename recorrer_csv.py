# liberias de panda
import pandas as pd 

pd.read_csv(filepath_or_buffer = "maqueta.csv") 

data = pd.read_csv(r"maqueta.csv",sep=';')   
df = pd.DataFrame(data, columns= ["Email","Id_Company","Nombre","Apellido","TelExt","CelEmp","NomCargo","Pagina Web","Ciudad","Departamento",
"NomCC","Pais","Codigo postal"])
email=pd.DataFrame(data, columns= ["Email"])

cols = "','".join([str(i) for i in df.columns.tolist()])
print(cols)


##### reparador de codigo 2
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Cobartram016\TRABDSP10;'
                      'Database=BDVIAJE2;'
                      'UID=tra-sap;'
                      'PWD=12345.TS;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()

for i,row in df.iterrows():
    sql = "INSERT INTO 'DC_Usuarios' ('" +cols + "') VALUES (" + "%s,"*(len(row)-1) + "%s)" 
    print(tuple(df))

cursor.execute(sql, tuple(df))  
#cursor.execute('''
 #               INSERT INTO DC_Usuarios(correo, id_company, nombres,apellidos,extension,celular,puesto,pagina_web,ciudad,departamento,area,pais,codigo_postal)
  #              VALUES
   #             ('pu@gmail.com',1,'pueba_un','dos' ,'52234','32122233','analista_base','www.google.com.co','barranquilla','atlantico','gdi','colombia','111111'),
    #            ('pue@gmail.com',1,'pueba_os','tres','52231','3121111','analista_junior','www.google.com.co','barranquilla','atlantico','gdi','colombia','11111')
     #           ''')
conn.commit()  



##### reparador de codigo 3
import pymssql
import pandas as pd


conn = pymssql.connect(host='Cobartram016\TRABDSP10', user='tra-sap', password='12345.TS', database='BDVIAJE2')
cur = conn.cursor()
 
 
# ------------------------------
# -- Create SQL
# ------------------------------
sql = "INSERT INTO DC_Usuarios values(%d, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s, %s, %s);"
data = [tuple(x) for x in df.values]
 
print("sql:", sql)
print("data:", data)
print (",,, sql_statement", "," * 100, "\n")
 
 
# ------------------------------
# -- Execute SQL
# ------------------------------
cur.executemany(sql, data)
conn.commit()

#ejecutar select verificar usuarios agregados
cursor.execute("SELECT * FROM DC_Usuarios Where correo='pu@gmail.com'")
for row in cursor:
    print(row)
