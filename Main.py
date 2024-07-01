import Funciones as F
op="0"
Diccionario=[]
listajugadores=[]
while True:
    print("Marcador de eShirlitos")
    print("1. Registrar puntajes torneo")
    print("2. Listar los todos puntajes")
    print("3. Imprimir por Tipo ")
    print("4. Salir del programa")
    op=input("Ingrese su opcion: ")   
    if op=="1":
        F.Registrar_puntajes_torneo()               
    elif op=="2":
        F.Listar_puntajes()           
    elif op=="3":
        F.Imprimir_por_Tipo()         
    elif op=="4":
        print("Saliendo del progama, hasta luego")
        break
    else:
        print("opcion ingresada no esta en el rango de 1 a 4")