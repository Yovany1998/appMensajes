# -*- coding: utf-8 -*-
# Programa: player.py
# Objetivo: simular el funcionamiento de un buzon de mensajes
# Autor: Yovany Hernandez Garcia
# Fecha: 01/03/2020
import sys
import os
import platform
from audioFile import AudioFile
class ShortMessageService:

    def __init__(self):
        """ Inicializa una lista de reproducción """
        self.my_inbox = list()
        # Diccionarios
        # Objetos que almacenan información en pares (clave y valor)
        self.options = {"1": self.add_message,
                        "2": self.message_count,
                        "3": self.get_unread_indexe,
                        "4": self.get_message,
                        "5": self.delete_messag,
                        "6": self.get_message,
                        "7": self.clear
                        }
  def menu(self):
        """ Despliega el menú principal. """
        self.clear_screen()
        print("""
                Reproductor musical
                
                1. Insertar un nuevo mensaje 
                2. Cantidad total de mensajes sms en buzon
                3. Listar todos los SMS sin leer
                4. Buscar mensaje
                5. Eliminar mensaje
                6. Vaciar papelera
                7.Salir
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

    def add_message(self):
        """ Agrega un nuevo mensaje. """
        print("\n======= Agregar mensaje =======")
        print("---------------------------------------------------------")
        self.my_inbox.append(
            input("Ingrese el nombre de la canción: "))
        self.press_enter()

  


if __name__ == "__main__":
    player = Player()
    player.run()

