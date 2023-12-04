import sqlite3
#BASE DE DATOS

def crear_base_datos_ranking():
    with sqlite3.connect("juego/bd_ranking.db") as conexion:
        try:

        # Crear la tabla si no existe
            sentencia = ('''CREATE TABLE puntajes 
                            (
                                    nombre TEXT,
                                    score INTEGER
                            )
                        ''')
            conexion.execute(sentencia)
            print("Se creo la tabla de puntajes")
        except sqlite3.OperationalError:
            print("La tabla de puntajes ya existe")

def guardar_puntaje(nombre_jugador, score):
    with sqlite3.connect("juego/bd_ranking.db") as conexion:
        cursor = conexion.execute("SELECT nombre FROM puntajes WHERE nombre = ?", (nombre_jugador,))
        existe_nombre = cursor.fetchone()

        if existe_nombre:
            try:
                conexion.execute("UPDATE puntajes SET score = ? WHERE nombre = ?", (score, nombre_jugador))
                conexion.commit()
                print(f"Se actualizó el score para '{nombre_jugador}' correctamente.")
            except sqlite3.Error:
                print(f"Error al actualizar el score de '{nombre_jugador}'")
        else:
            try:
                conexion.execute("INSERT INTO puntajes (nombre, score) VALUES (?, ?)", (nombre_jugador, score))
                conexion.commit()
                print("Se agregó el score correctamente.")
            except sqlite3.Error :
                print(f"Error al insertar el score de '{nombre_jugador}'")

def obtener_top_5_puntajes():
    with sqlite3.connect("juego/bd_ranking.db") as conexion:
        cursor = conexion.execute("SELECT nombre, score FROM puntajes ORDER BY score DESC LIMIT 5")
        top_5_puntajes = cursor.fetchall()  # Obtener los 5 mejores puntajes
        
            
        return top_5_puntajes

def eliminar_tabla():
    with sqlite3.connect("juego/bd_ranking.db") as conexion:
        try:
            # Ejecutar una sentencia DROP TABLE para eliminar la tabla completa
            conexion.execute("DROP TABLE IF EXISTS puntajes")
            conexion.commit()  # Agrega esto para confirmar los cambios
            print("Se eliminó la tabla correctamente.")
        except sqlite3.Error as e:
            print(f"Error al eliminar la tabla: {e}")
