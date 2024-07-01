
def Registrar_puntajes_torneo():
        listajugadores=[]
        id=input("Ingrese su id de juego: ")
        nya=input("Ingrese su nombre y apellido:")
        while True:
            try:
                pvalo=int(input("Ingrese su puntaje de valorant: "))
                if pvalo<0:
                    print("Puntaje valorant tiene que ser mayor o igual a 0")
                else:
                    break
            except:
                print("El dato ingresado tiene que ser un digito")
        while True:
            try:
                pfort=int(input("Ingrese su puntaje de fortnite: "))
                if pfort<0:
                    print("Puntaje fortnite tiene que ser mayor o igual a 0")
                else:
                    break
            except:
                print("El dato ingresado tiene que ser un digito")
        while True:
            try:
                pfifa=int(input("Ingrese su puntaje de fifa: "))
                if pfifa<0:
                    print("Puntaje fortnite tiene que ser mayor o igual a 0")
                else:
                    break
            except:
                print("El dato ingresado tiene que ser un digito")
        tipo=input("Seleccione su tipo\n1. Principiante \n2. Avanzado \n3. Experto\n Ingrese su opcion: ")
        if tipo=="1":
            tipo="Principiante"
            Diccionario= {
                        "Id_Jugador":id, 
                        "Nombre y apellido":nya, 
                        "Puntaje Valorant":pvalo, 
                        "Puntaje Fortnite":pfort, 
                        "Puntaje Fifa":pfifa, 
                        "Tipo":tipo
                          }
            for key, value in Diccionario.items():
                listajugadores.append(key, value)
                with open("Archivo.txt", "w", newline="\n") as archivo:
                    archivo.write(listajugadores)
                    print("Archivo guardado con exito")
        elif tipo=="2":
            tipo="Avanzado"
            Diccionario= {
                        "Id_Jugador":id, 
                        "Nombre y apellido":nya, 
                        "Puntaje Valorant":pvalo, 
                        "Puntaje Fortnite":pfort, 
                        "Puntaje Fifa":pfifa, 
                        "Tipo":tipo
                          }
            for key, value in Diccionario.items():
                listajugadores.append(key, value)
                with open("Archivo.txt", "w", newline="\n") as archivo:
                    archivo.write(listajugadores)
                    print("Archivo guardado con exito")
        elif tipo=="3":
            tipo="Experto"
            Diccionario= {
                        "Id_Jugador":id, 
                        "Nombre y apellido":nya, 
                        "Puntaje Valorant":pvalo, 
                        "Puntaje Fortnite":pfort, 
                        "Puntaje Fifa":pfifa, 
                        "Tipo":tipo
                          }
            for key, value in Diccionario.items():
                listajugadores.append(key, value)
                with open("Archivo.txt", "w", newline="\n") as archivo:
                    archivo.write(listajugadores)
                    print("Archivo guardado con exito")
        else:
            print("Opcion ingresada no valida")
        
def Listar_puntajes(listajugadores):
    print(listajugadores)

def Imprimir_por_Tipo():
    
    opc=input("Seleccione el tipo de dificultad que desea ver la lista de jugadores\n1. Principiante \n2. Avanzado \n3. Experto\n Ingrese su opcion: ")
    if opc=="1":
        with open("datos.txt", "r") as archivo:
            archivo.read
            for dificultad in archivo("Tipo"):
                if dificultad=="Principiante":
                    print(listajugadores)
    elif opc=="2":
        with open("datos.txt", "r") as archivo:
            archivo.read
            for dificultad in archivo("Tipo"):
                if dificultad=="Avanzado":
                    print(listajugadores)
    elif opc=="3":
        with open("datos.txt" , "r") as archivo:
            archivo.read
            for dificultad in archivo("Tipo"):
                if dificultad=="Experto":
                    print(listajugadores)
    else:
         print("opcion no valida")