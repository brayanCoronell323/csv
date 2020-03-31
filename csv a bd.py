import pyodbc
import pandas as pd 
#variables para la conexion
direccion_servidor = 'Cobartram016\TRABDSP10'
nombre_bd = 'BDVIAJE2'
nombre_usuario = 'tra-sap'
password = '12345.TS'

#validador de conexion
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("Conexion establecida")
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
        
        
#variable para crear sentencias 
conn = conexion
 
cursor = conn.cursor()

#leer csv
pd.read_csv(filepath_or_buffer = "maqueta.csv") 
#indentificardor de objeto que separa el csv de un dato a otro
data = pd.read_csv(r"maqueta.csv",sep=';')
#leer datos importante del csv y agregarlos en un dataframe
df = pd.DataFrame(data, columns= ["Email","Id_Company","Nombre","Apellido","TelExt","CelEmp","NomCargo","Pagina Web","Ciudad","Departamento",
"NomCC","Pais","Codigo postal"])
#dato de prueba
email=pd.DataFrame(data, columns= ["Email"])


prueba=df["Email"][1]
#variable de columnas de la base de datos
colss='correo','id_company','nombres','apellidos','extension','celular','puesto','pagina_web','ciudad','departamento','area','pais','codigo_postal'


for i,row in df.iterrows():
        try:
            sql = "INSERT INTO  DC_Usuarios (correo, id_company, nombres,apellidos,extension,celular,puesto,pagina_web,ciudad,departamento,area,pais,codigo_postal) VALUES (" + "?,"*(len(row)-1) + "?)" 
            #print(sql)
            print(tuple(row))
            cursor.execute(sql, tuple(row))

    
        except Exception as e:
            cursor.execute("SELECT top 1 * FROM DC_Usuarios")
            columnas =cursor.description
            cols = [col[0] for col in columnas]
            aux=list(row[1:])
            aux.append(row[0])
            update= "UPDATE DC_Usuarios set ["+']=?,['.join(cols[1:])+"]=? where ["+cols[0]+"]=?"
            cursor.execute(update,tuple(aux))
            #print(Postal_Code)
            #print(aux)