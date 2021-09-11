import random as rd
import pyperclip as clip
import re
import os
import sys

class app():

    def exec(self, route = "0"):

        choice = input("Bienvenido al generador de contraseñas, que desea hacer?\n"\
                        "1. Generar una contraseña completamente del sistema\n"
                        "2. Incluir palabras de mi eleccion en la contraseña\n"\
                        "3. Salir\n\n"\
                        "Opcion: ") if route == "0" else route

        self.clear_screen()

        if choice == "1":
            
            length = input("Longitud de la contraseña (max. 16, solo numeros): ")

            if length.isnumeric() and int(length) <= 16:

                password = self.generator_simple(int(length))
                print(f"\n{password}\n")
                wait = self.copy(password)
                self.clear_screen(wait = wait)
                self.exec()
            
            else:

                print("Parametros incorrecos, ingreselos de nuevo")
                self.clear_screen(True)
                self.exec("1")

        elif choice == "2":

            length = input("Longitud de la contraseña (max. 16, solo numeros): ")

            if length.isnumeric() and int(length) <= 16:

                words = input("\nIncluya la(s) palabra(s) que desea incluir separadas por un espacio(' '),\n"\
                            "tenga en cuenta que la suma de estas\n"\
                            "no pueden ser mas largas a 3/4 de la longitud de la contraseña\n\n"\
                            "Palabra(s): ")

                self.clear_screen()
                included = re.split(" ", words)
                total = self.check_length(len("".join(included)), int(length))

                if total:

                    password = self.generator_input(included, int(length))
                    print(f"\n{password}\n")
                    wait = self.copy(password)
                    self.clear_screen(wait = wait)
                    self.exec()

                else:

                    print("Parametros incorrectos, ingreselos como se le indica")
                    self.clear_screen(True)
                    self.exec("2")
            
            else:

                print("Parametros incorrectos, ingreselos como se le indica")
                self.clear_screen(True)
                self.exec("2")
    
        elif choice == "3":

            self.clear_screen()
            sys.exit()

    def check_length(self, to_include, length):

        return True if to_include <= (int(length)/4)*3 else False

    def generator_simple(self, length):

        letters = "abcdefghijklmnñopqrstuvwxyz"
        num = "0123456789"
        sym = r"~`!@#$%^&*()_+=-][{}|\:;''<,>.?/"
        together = "".join(list(rd.sample("".join([letters.upper(),letters, num, sym]), int(length))))

        return together

    def generator_input(self, words, length):

        letters = "abcdefghijklmnñopqrstuvwxyz"
        num = "0123456789"
        sym = r"~`!@#$%^&*()_+=-][{}|\:;''<,>.?/"
        to_include = length - len(words)
        div = [rd.randint(0, to_include) for times in range(len(words))]
        div.sort()
        password = "".join(list(rd.sample("".join([letters.upper(),letters, num, sym]), to_include)))
        end = ""
        count = 0

        for chars in password:

            if count in div:

                end += words[div.index(count)]

            else:

                end += chars

            count += 1

        return end

    def copy(self, word):

        choice = input("Desea copiarla al portapapeles? [y/n]: ")

        if choice == "y":

            clip.copy(word)
            print("Copiado al portapapeles")

            return True

        return False

    def clear_screen(self, wait = False):

        if wait == True:

            os.system("Pause")

        if os.name == "nt":

            os.system("cls")
        
        else:

            os.system("clear")


app().exec()