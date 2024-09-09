##Arreglo 

arr = []
count = 0


## Menu

def mostrar_menu():
    print("\n**** Registro de libros ****")
    print("\n**** 1: Ingresar el titulo, autor, editorial, género y descripción ****")
    print("\n**** 2: Ingresar el precio y cantidad ****")
    print("\n**** 3: Eliminar libro ****")
    print("\n**** 4: Mostrar arreglo ****")
    print("\n**** 5: Salir ****")
    print("\n**** En la opción 1 debe ingresar en orden los siguientes datos: ****")
    print("\n**** Título, Autor, Editorial, Género, Descripción ****")
    print("\n**** En la opción 2 debe ingresar en orden los siguientes datos: ****")
    print("\n**** Precio y Unidades ****")
    print("\n**** Registro de libros ****")
    print("\n ")

#Ingresar información opción 1
def insertar_libro():
    valor = input("Ingrese la información según orden opción 1: ")
    arr.append(valor)
    print("Nombre información ingresada de manera exitosa!")
    

#Ingresar información opción 2
def insertar_libro_2():
    valor = int(input("Ingrese la información según orden opción 2: "))
    arr.append(valor)
    print("Nombre información ingresada de manera exitosa!")


#eliminar libro
def eliminar_libro():
    indice = int(input("Ingrese el índice del libro a borrar: "))

#Verificación del arreglo
def mostrar_datos():
    print("datos ingresados:", arr)



#Menu e ingreso de datos
while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        insertar_libro()
    elif opcion == 2:
        insertar_libro_2()
    elif opcion == 3:
        eliminar_libro()    
    elif opcion == 4:
        mostrar_datos()
    elif opcion == 5:
        print("Nos veremos!")
        break
    else:
        print("Opción no válida. Ingrese los datos nuevamente.")

#Cambiar la variable arreglo por libro_1 para que se distinga de los nuevos ingresos
#Realizar este paso cada ves que se reasigne la variablee arr hasta alcanzar el libro 50.
libro_1 = arr
libro_2 = arr
libro_3 = arr
#....
libro_50 = arr

