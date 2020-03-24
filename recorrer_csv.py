# liberias de panda
import pandas as pd 
import pyodbc 

#leer archivo csv de datos
pd.read_csv(filepath_or_buffer = "maqueta.csv") 
#dar tabulacion del csv con ;
data = pd.read_csv(r"maqueta.csv",sep=';') 
#campos a elegir del csv  
df = pd.DataFrame(data, columns= ["Email","Id_Company","Nombre","Apellido","TelExt","CelEmp","NomCargo","Pagina Web","Ciudad","Departamento",
"NomCC","Pais","Codigo postal"])

cols = "','".join([str(i) for i in df.columns.tolist()])
print(df)

#Conexion a la base de datos
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Cobartram016\TRABDSP10;'
                      'Database=BDVIAJE2;'
                      'UID=tra-sap;'
                      'PWD=12345.TS;'
                      'Trusted_Connection=yes;')
 

cursor = conn.cursor()

#ciclo repetivo para ingresar datos de cvs a la base de datos
for i,row in df.iterrows():
    sql = "INSERT INTO DC_Usuarios (correo, id_company, nombres,apellidos,extension,celular,puesto,pagina_web,ciudad,departamento,area,pais,codigo_postal) VALUES (" + "?,"*(len(row)-1) + "?)" 
    print(sql)
    print(tuple(row))
    cursor.execute(sql, tuple(row))
    
conn.commit() 
input()