import os
import sys
import json
from json.decoder import JSONDecodeError

# Program which manages a simple database (a Python dictionary stored in a file)

class Database():
    """ Clase que modela la BD sobre la que trabaja el programa. Incluye los métodos necesarios para cargarla y actualizarla en el disco"""
    def __init__(self,nombre_fichero):
        """Inicializa el objeto BD y carga en memoria los datos"""
        self.nombre_fichero = nombre_fichero
        self.diccionario = {}
        self.__cargar_archivo()

    def __comprobar_archivo(self):
        """Comprueba si existe el archivo. En caso afirmativo, devuelve True. En caso negativo, lo crea y devuelve False."""
        if(not(os.path.isfile(nombre_archivo))):
            with open(nombre_archivo,'w') as archivo:
                archivo.close
            return False
        else:
            return True # sí que existe el archivo    

    def __cargar_archivo(self):
        """Carga la BD en la memoria RAM"""
        if(self.__comprobar_archivo()):
            try:
                archivo = open(nombre_archivo,'r')
                self.diccionario.update(json.load(archivo))
                archivo.close
            except JSONDecodeError:
                print('Error reading the JSON file: wrong format')
                sys.exit(1) # termina la ejecución del programa con error
            except Exception:
                print('Error reading the database')
                sys.exit(1) # termina la ejecución del programa con error

    """Métodos públicos de la clase: CRUD"""           
    
    def actualizar_archivo(self):
        """Actualiza el archivo de texto en el que se almacena la BD"""
        archivo = open(nombre_archivo,'w')
        archivo.write(json.dumps(self.diccionario))
        archivo.close       

    def crear_entrada(self,clave, valor):
        """Añade una entrada al diccionario con la clave y valor especificados"""
        if(clave in self.diccionario):
            print("There is already an entry with the key " + clave)
        else:
            # No hay entradas con esa clave
            self.diccionario[clave] = valor
            print("Entry successfully created")
            self.actualizar_archivo()  
           
    def ver_entradas(self):
        """Muestra en pantalla las entradas del diccionario"""
        print("Number of entries: " + str(len(self.diccionario)) + '\n')
        for clave,valor in self.diccionario.items():
            print(('\t %s --> %s') %(clave,valor))

    def eliminar_entrada(self,clave):
        """Elimina del diccionario la entrada con la clave especificada"""
        if(clave in self.diccionario):
            del self.diccionario[clave]
            print(('Entry with key "%s" successfully deleted' %(clave,)))
            self.actualizar_archivo()
        else:
            # No existe ninguna entrada con esa clave
            print("No entry in the database with key " + clave)

    def modificar_entrada(self,clave):
        """Modifica una entrada ya creada en el diccionario"""      
        if(clave in self.diccionario):
            nuevo_valor = input("Insert a new value for " + clave + ": ")
            self.diccionario[clave] = nuevo_valor
            print('Entry updated')
            self.actualizar_archivo()
        else:
            # No existe ninguna entrada con esa clave
            print("No entry in the database with key " + clave)                 

# Carga la base de datos desde el fichero de texto
nombre_archivo = 'file.json' # nombre por defecto
if(len(sys.argv)==2):
    nombre_archivo = sys.argv[1] # nombre de fichero especificado en los argumentos del programa

base_datos = Database(nombre_archivo)

def mostrar_menu():
    """Muestra un menú para que el usuario pueda interactuar con la aplicación"""
    print("Database: " + nombre_archivo)
    while(True):
        print("\nChoose an option: ")     
        print("1) Read entries in the DB")
        print("2) Create a new entry in the DB")
        print("3) Delete entry from the DB")
        print("4) Modify entry from the DB")
        print("0) Exit")
        seleccion = input("Option: ")
        if(not(seleccion.isdigit())):
            print("Wrong option. Try again.")
        else:
            # Comprueba la opción elegida
            if(int(seleccion)==1):
                # Ver entradas en la BD
                print('\n')
                base_datos.ver_entradas()
            elif(int(seleccion)==2):
                # Crear nueva entrada en la BD
                clave = input('\nType the key: ')
                valor = input('Type the value: ')
                base_datos.crear_entrada(clave, valor)
            elif(int(seleccion)==3):
                # Eliminar entrada de la BD
                print('\n')
                clave = input("Key of the entry you want to delete: ")
                base_datos.eliminar_entrada(clave)
            elif(int(seleccion)==4):
                # Modificar entrada de la BD
                print('\n')
                clave = input("Key of the entry you want to modify: ")
                base_datos.modificar_entrada(clave)
            elif(int(seleccion)==0):
                # Salir del programa       
                sys.exit(0)
            else:
                # Selección no válida
                print("Wrong selection. Try again.")

# Muestra el menú de usuario
mostrar_menu()
