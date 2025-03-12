#software estructuras
nombreVendedor="Ana Maria"
productos=[]
producto={}

#CREANDO UN CICLO EN PYTHON
opcion=100
print("Merqueo App")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("5. Salir")

while opcion != 5:
    print("estoy adentro")
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        #CREANDO CLAVES Y VALORES DE UN DICCIONARIO
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("¿Cual presentacion deseas? ")

        #MOSTRANDO MI DICCIONARIO
        #print(producto)

        #POBLANDO UNA LISTA (AGREGANDO ELEMENTOS A UNA LISTA), LLAMAR LA LISTA SI ESTA EN PLURAL ES UNA LISTA, SI ESTA EN SINGULAR ES DICCIONARIO
        productos.append(producto) ##AGREGAR ELEMENTOS A LA LISTA
        print(productos)

    elif opcion == 2:
        #UTILIZANDO CICLOS FOR EN PYTHON PARA RECORRER LISTAS
        for productoSeleccionado in productos:
            print(productoSeleccionado["nombre"])
        print("Estoy en la dos")
    elif opcion == 3:
        #0. PREGUNTAR A QUIEN QUIERES EDITAR
        productoCambio=int(input("Digita el id del producto a editar:"))
        #1. ENCONTRAR EL ELEMENTO
        for productoBuscado in productos:
            if productoBuscado["id"]==productoCambio:
                print("Encontrado")
            else:
                print("No lo encontre")
        #2. SELECCIONO EL ELEMENTO 
        #3. ACCEDO A LAS PROPIEDADES O ATRICUTOS QUE QUIERO O PUEDO MODIFICAR
        print("Estoy en la tres")
    elif opcion == 4:
        print("Estoy en la cuatro")
    else:
        print("Opcion invalida")