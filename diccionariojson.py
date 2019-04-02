import os
import sys
import json
from json.decoder import JSONDecodeError

# Programa que gestiona una base de datos simple (un diccionario almacenado en un fichero)

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
                print('Error al leer el fichero JSON: formato incorrecto')
                sys.exit(1) # termina la ejecución del programa con error
            except Exception:
                print('Error ineseperado al leer la base de datos')
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
            print("Ya existe una entrada con la clave " + clave)
        else:
            # No hay entradas con esa clave
            self.diccionario[clave] = valor
            print("Entrada creada correctamente")
            self.actualizar_archivo()  
           
    def ver_entradas(self):
        """Muestra en pantalla las entradas del diccionario"""
        print("Número de entradas: " + str(len(self.diccionario)) + '\n')
        for clave,valor in self.diccionario.items():
            print(('\t %s --> %s') %(clave,valor))

    def eliminar_entrada(self,clave):
        """Elimina del diccionario la entrada con la clave especificada"""
        if(clave in self.diccionario):
            del self.diccionario[clave]
            print(('Entrada con clave "%s" borrada correctamente' %(clave,)))
            self.actualizar_archivo()
        else:
            # No existe ninguna entrada con esa clave
            print("No existe ninguna entrada con la clave " + clave)

    def modificar_entrada(self,clave):
        """Modifica una entrada ya creada en el diccionario"""      
        if(clave in self.diccionario):
            nuevo_valor = input("Introduzca el nuevo valor para " + clave + ": ")
            self.diccionario[clave] = nuevo_valor
            print('Entrada actualizada')
            self.actualizar_archivo()
        else:
            # No existe ninguna entrada con esa clave
            print("No existe ninguna entrada con la clave " + clave)                 

# Carga la base de datos desde el fichero de texto
nombre_archivo = 'archivo.json' # nombre por defecto
if(len(sys.argv)==2):
    nombre_archivo = sys.argv[1] # nombre de fichero especificado en los argumentos del programa

base_datos = Database(nombre_archivo)

def mostrar_menu():
    """Muestra un menú para que el usuario pueda interactuar con la aplicación"""
    print("Base de datos: " + nombre_archivo)
    while(True):
        print("\nSelecciona una opción: ")     
        print("1) Ver entradas en la BD")
        print("2) Crear nueva entrada en la BD")
        print("3) Eliminar entrada de la BD")
        print("4) Modificar entrada de la BD")
        print("0) Salir del programa")
        seleccion = input("Opción: ")
        if(not(seleccion.isdigit())):
            print("Selección incorrecta. Inténtelo de nuevo.")
        else:
            # Comprueba la opción elegida
            if(int(seleccion)==1):
                # Ver entradas en la BD
                print('\n')
                base_datos.ver_entradas()
            elif(int(seleccion)==2):
                # Crear nueva entrada en la BD
                clave = input('\nIntroduzca la clave: ')
                valor = input('Introduzca el valor: ')
                base_datos.crear_entrada(clave, valor)
            elif(int(seleccion)==3):
                # Eliminar entrada de la BD
                print('\n')
                clave = input("Clave de la entrada que desea eliminar: ")
                base_datos.eliminar_entrada(clave)
            elif(int(seleccion)==4):
                # Modificar entrada de la BD
                print('\n')
                clave = input("Clave de la entrada que desea modificar: ")
                base_datos.modificar_entrada(clave)
            elif(int(seleccion)==0):
                # Salir del programa       
                sys.exit(0)
            else:
                # Selección no válida
                print("Selección incorrecta. Inténtelo de nuevo.")

# Muestra el menú de usuario
mostrar_menu()
