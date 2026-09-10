print ("Esto es un manipulador de matrices, elegi lo que queres hacer, de preferencia primero carga la matriz, no seas bobi")
respuesta=int(input(f"ingresa lo que queres hacer:\n 1) Cargar matriz.\n 2) Mostrar matriz.\n 3) Sumatoria.\n 4) Productoria.\n 5) Transpuesta.\n")) 
filas=1
columnas=1
matriz=[]
while True:
    if respuesta==1:
        matriz=[]
        filas=int(input("Ingrese la cantidad de filas: "))
        columnas=int(input("Ingrese la cantidad de columnas: "))
        for i in range(filas):
            fila=[]
            for j in range(columnas):
                elemento=int(input(f"Ingrese el elemento [{i}][{j}]: "))
                fila.append(elemento)
            matriz.append(fila)
        respuesta=int(input(f"ingresa lo que queres hacer:\n 1) Cargar matriz.\n 2) Mostrar matriz.\n 3) Sumatoria.\n 4) Productoria.\n 5) Transpuesta.\n"))            
    elif respuesta==2:
        print("La matriz es:")
        for fila in matriz:
            print(f"Fila {i}:{fila}")
        respuesta=int(input(f"ingresa lo que queres hacer:\n 1) Cargar matriz.\n 2) Mostrar matriz.\n 3) Sumatoria.\n 4) Productoria.\n 5) Transpuesta.\n"))
    elif respuesta==3:
        sumatrices=0
        for i in range(filas):
            for j in range(columnas):
                sumatrices+=matriz[i][j]
        print(f"La suma de todos los elementos de la matriz es: {sumatrices}")
        respuesta=int(input(f"ingresa lo que queres hacer:\n 1) Cargar matriz.\n 2) Mostrar matriz.\n 3) Sumatoria.\n 4) Productoria.\n 5) Transpuesta.\n"))
    elif respuesta==4:
        productor=1
        for i in range(filas):
            for j in range(columnas):
                productor*=matriz[i][j]
        print(f"El producto de todos los elementos de la matriz es: {productor}")
        respuesta=int(input(f"ingresa lo que queres hacer:\n 1) Cargar matriz.\n 2) Mostrar matriz.\n 3) Sumatoria.\n 4) Productoria.\n 5) Transpuesta.\n"))
    elif respuesta==5:
        matriztras=[]
        for j in range(columnas):
            filatrans=[]
            for i in range(filas):
                filatrans.append(matriz[i][j])
            matriztras.append(filatrans)

        print("La matriz transpuesta es:")
        for fila in matriztras:
            print(fila)
        respuesta=int(input(f"ingresa lo que queres hacer:\n 1) Cargar matriz.\n 2) Mostrar matriz.\n 3) Sumatoria.\n 4) Productoria.\n 5) Transpuesta.\n"))
    else:
        print("Opcion invalida: Ingresa un número del 1 al 5, gil.")