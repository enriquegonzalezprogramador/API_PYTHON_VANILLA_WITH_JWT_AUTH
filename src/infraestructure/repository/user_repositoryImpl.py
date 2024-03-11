import psycopg2
from infraestructure.orm import Database
from domain.repository.user_repository import UserRepository
from domain.user import User
import json

class UserRepositoryImpl(UserRepository):
    def get_all(self):
        try:
            connection = Database().db_session()
            cursor = connection.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            users = cursor.fetchall()

            # Convertir los resultados en formato JSON sin escapar
            json_users = json.dumps([dict(zip(['id', 'name', 'edad', 'sexo', 'pais'], user)) for user in users], ensure_ascii=False)
            
            print(json_users)  # Imprime la cadena JSON en la consola de Python
            
            return json_users
        except psycopg2.Error as e:
            # Manejo de errores en caso de problemas con la base de datos
            print("Error al obtener todos los usuarios:", e)
            return None
        finally:
            connection.close()

    def get_by_id(self, user_id):
        try:
            connection = Database().db_session()
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()

            # Verificar si se encontró un usuario con el ID especificado
            if user:
                # Convertir el resultado en un diccionario
                user_dict = dict(zip(['id', 'name', 'edad', 'sexo', 'pais'], user))
                # Convertir el diccionario en formato JSON sin escapar
                json_user = json.dumps(user_dict, ensure_ascii=False)
                return json_user
            else:
                print("No se encontró ningún usuario con el ID especificado:", user_id)
                return None
        except psycopg2.Error as e:
            # Manejo de errores en caso de problemas con la base de datos
            print(f"Error al obtener el usuario con ID {user_id}:", e)
            return None
        finally:
            connection.close()

    def create(self, user_data):
        try:
            connection = Database().db_session()
            cursor = connection.cursor()

            # Insertar los datos del usuario en la base de datos
            query = "INSERT INTO users (name, edad, sexo, pais) VALUES (%s, %s, %s, %s) RETURNING id"
            cursor.execute(query, (user_data['name'], user_data['edad'], user_data['sexo'], user_data['pais']))
            new_user_id = cursor.fetchone()[0]
            connection.commit()

            print("Usuario creado con el ID:", new_user_id)
            return new_user_id
        except psycopg2.Error as e:
            # Manejo de errores en caso de problemas con la base de datos
            print("Error al crear un nuevo usuario:", e)
            return None
        finally:
            connection.close()

    def update(self, user_id, user_data):
        try:
            connection = Database().db_session()
            cursor = connection.cursor()

            # Actualizar los datos del usuario en la base de datos
            query = "UPDATE users SET name = %s, edad = %s, sexo = %s, pais = %s WHERE id = %s"
            cursor.execute(query, (user_data['name'], user_data['edad'], user_data['sexo'], user_data['pais'], user_id))
            connection.commit()

            print("Usuario actualizado correctamente")
            return True
        except psycopg2.Error as e:
            # Manejo de errores en caso de problemas con la base de datos
            print(f"Error al actualizar el usuario con ID {user_id}:", e)
            return False
        finally:
            connection.close()

    def delete(self, user_id):
        try:
            connection = Database().db_session()
            cursor = connection.cursor()

            # Eliminar el usuario de la base de datos
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            connection.commit()

            print("Usuario eliminado correctamente")
            return True
        except psycopg2.Error as e:
            # Manejo de errores en caso de problemas con la base de datos
            print(f"Error al eliminar el usuario con ID {user_id}:", e)
            return False
        finally:
            connection.close()


