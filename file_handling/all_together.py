
print("Bienvenido al programa")
user_input = ""

def write_file():
      file = open("file_handling/demo_two.txt","a")
      user_content = input("ingresa el contenido\n")
      file.write(user_content + "\n")
      file.close()

def read_file():
  file = open("file_handling/demo_two.txt","r")
  for line in file:
    print(line)       

def print_menu():
    print("##############")
    print("ingrsa una opcion")
    print("1","agregar contenido")
    print("2", "leer contenido")
    print("exit", "para salir")
    print("##############")


while user_input != "exit":
    print_menu()
    user_input = input()

    if user_input == "1":
        write_file()
    elif user_input == "2":
      read_file()
    elif user_input == "exit":
      print("chau chau")
      exit()  
    else:
      print("opcion incorrecta")

      