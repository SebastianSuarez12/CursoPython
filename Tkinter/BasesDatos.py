import psycopg2

# 1. Establecer la conexión con la base de datos
conexion = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='root', port=5432)
# 2. Creamos el cursos
cursor = conexion.cursor()
# Ejecutamos
cursor.execute('SELECT * FROM public."Usiarios";')
# Visualizar los resultados
for data in cursor.fetchall():
    print(data)

# Insert (sentencia insert) (valores)

sentenciaInsert = '''INSERT INTO public."Usiarios"(
	nombre, apellido, edad, sexo, correo, formacion)
	VALUES (%s, %s, %s, %s, %s, %s, %s);
    '''
valores = ('22','Anderson2','Cardenas',22,'M', 'elpepe@gmail.com', 'Superior')

cursor.execute(sentenciaInsert,valores)
conexion.commit()
registrosInsertados = cursor.rowcount
print('Se insertaron ', registrosInsertados)
