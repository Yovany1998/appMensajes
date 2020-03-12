# -*- coding: utf-8 -*-
# Programa: player.py
# Objetivo: simular el funcionamiento de un buzon de mensajes
# Autor: Yovany Hernandez Garcia
# Fecha: 01/03/2020
import sys
import os
import platform
#from audioFile import AudioFile
class ShortMessageService:
    

    def __init__(self):
        """ Inicializa las listas """
        self.has_been_viewed = []
        self.my_inbox = list()
        # Diccionarios
        # Objetos que almacenan información en pares (clave y valor)
        self.options = {"1": self.add_new_arriva,
                        "2": self.message_count,
                        "3": self.get_message,
                        "4": self.get_unread_indexe,
                        "5": self.delete_message,
                        "6": self.clear,
                        "7": self.close
                        }

    def menu(self):
        """ Despliega el menú principal. """
        self.clear_screen()
        print("""
                        Mensajes
                
                1. Insertar un nuevo mensaje 
                2. Cantidad total de mensajes sms en buzon
                3. Buscar mensaje  
                4. Listar todos los SMS sin leer 
                5. Eliminar mensaje
                6. Vaciar papelera
                7. Salir
                """)

    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiona Enter para continuar")

    def clear_screen(self):
        """
        Verifica mediante la librería platform el sistema operativo
        del usuario y limpia la pantalla dependiendo del SO utilizado.
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")

    def add_new_arriva(self):
        """ Agrega un nuevo mensaje. """
        print("\n======= Agregar mensaje =======")
        print("  Los mensajes deben ser ingresados de la siguiente manera : ")
        print("numeroTelefono, mensaje\")")
        print("---------------------------------------------------------")
        self.my_inbox.append(
            input("Ingrese el mensaje: "))
        self.has_been_viewed.append("False")
        self.press_enter()

    def message_count(self):
        """Cuenta y muestra la cantidad de mensajes que hay en la bandeja"""
        print("Tiene {0} mensajes".format(len(self.my_inbox)))        
        self.press_enter()  

    def get_unread_indexe(self, file_filter="", delete=False):
        """ Muestra todos los mensajes  """
        print(self.my_inbox)
        print(len(self.my_inbox))
        self.press_enter()

        return False


    def get_message(self, search_position="", delete=False):
        """Retorna el mensaje en la posición que se seleccione"""
        message = 0
        message_position = 0
        if search_position == "":
            print(self.my_inbox)
            print(len(self.my_inbox))
            search_position = int(
                    input("Ingresa la posición del mensaje: "))
        
        for x in range (len(self.my_inbox)):
            if self.my_inbox[x] != message:
                message = self.my_inbox[x]
                message_position = x + 1
                if message_position == search_position:
                    print("El mensaje {0} es: ".format(search_position))
                    print(self.my_inbox[x])
                    self.press_enter() if not delete else True
                
                    return True
        
        print("El mensaje no existe")                                    
        self.press_enter()  
        return False
        

    def delete_message(self):
        """Elimina el mensaje en la posición que se seleccione"""        
        search_position = int(
                    input("Ingresa la posición del mensaje: "))            
        if self.get_message(search_position, True):            
            try:
                self.my_inbox.remove(self.my_inbox[search_position-1])
                print("¡El mensaje {0} ha sido eliminado satisfactoriamente!"
                      .format(search_position))               
                self.press_enter()       
            except ValueError:
                print("¡El mensaje no se encuentra en la bandeja!")
                self.press_enter()

    def clear(self):
        """Elimina todos los mensajes """
        condition = int(input("¿Desea Eliminar todos los mensajes? si(1)/no(0)"))
        if condition == 1:
            self.my_inbox[:]=[]
            print("Mensajes Eliminados Satisfactoriamente")
            self.press_enter()
        elif condition == 0:
            print("¡Los mensajes no han sido eliminados!")
            self.press_enter()
        else:
            print("¡Comando invalido!")
            self.press_enter() 

    def close(self):
        """ Cierra la mensajeria. """
        sys.exit(0)

    def run(self):
        """ Despliega el menú principal y procesa las opciones. """
        while True:
            self.menu()
            choice = input("Ingrese una opción: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("¡{0} no es una opción vålida!".format(choice))
                self.press_enter()


if __name__ == "__main__":
    MSM = ShortMessageService()
    MSM.run()
