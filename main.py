# Lista para guardar la información de los usuarios (nombre, codigo , correo)
usuarios = []

# Lista para guardar la información de los libros (nombre libro, nombre autor, fecha de publicacion, numero de libros disponible)
libros = []

# Diccionario para registrar los préstamos: clave = código del usuario, valor = lista de libros prestados
prestos = {}

# Función para añadir un nuevo libro 
def anadir_libro():
    tab = []
    tab.append(input("Ingresar el nombre del libro: "))
    tab.append(input("Ingresar el nombre del autor: "))
    tab.append(int(input("Ingresar la fecha de publicacion: ")))
    tab.append(int(input("Ingresar el numero de libros disponible: ")))
    libros.append(tab)
    return tab

# Función para editar un libro 
def editar_libro():
    nombre = input("Ingresar el nombre del libro que quieres editar")
    for libro in libros:
        if nombre.lower() == libro[0].lower(): # Aqui buscamos el libro con su nombre
            print(libro)
            while True:
                num = int(input("Que quieres cambiar? : 1 = Cambiar nombre / 2 = Cambiar autor / 3 = Cambiar fecha publicacion / 4= Cambiar numero disponible"))
                match num :
                    case 1:
                        libro[0] = input("Ingresar el nuevo nombre")
                        break
                    case 2:
                        libro[1] = input("Ingresar el nuevo autor")
                        break
                    case 3:
                        libro[2] = int(input("Ingresar la nueva fecha"))
                        break
                    case 4: 
                        libro[3] = int(input("Ingresar el nuevo numero de libros disponible"))
                        break
                    case _:
                        print("Error ingrese un numero entre 1 y 4 ")
            break   
    else : 
        print("Libro no encontrado en la lista")
        
# Función para borrar un libro
def borrar_libro():
    nombre = input("Ingresar el nombre del libro que quieres borrar")
    for libro in libros:
        if nombre.lower() == libro[0].lower():  # Aqui buscamos el libro con su nombre
            libros.remove(libro)
            print(f" El libro fue borrado con exito")
            break
    else:
        print("Libro no encontrado en la lista ")
        
# Función para buscar un libro con su nombre o el nombre del autor        
def buscar_libro():
    num = int(input("Como quieres buscar?: ingresa 1: con el nombre del libro : ingresa 2: con el nombre del autor:  "))
    match num:
        case 1:
            nombre = input("Ingresar el nombre del libro que quieres buscar")
            for libro in libros:
                if nombre.lower() == libro[0].lower(): # Aqui buscamos el libro con su nombre
                    print("Libro encontrado sus informaciones son :")
                    print(libro)
                    return True , libro
            else:
                print("Libro no encontrado en la lista ")
                return False
        case 2:
            autor = input("Ingresar el nombre del autor que quieres buscar")
            numlibrosautor = 0
            librosautor = [] #Lista para guardar todo los libros del autor
            for libro in libros:
                if autor.lower() == libro[1].lower(): # Aqui buscamos todos los libros del autor
                    librosautor.append(libro)
                    numlibrosautor +=1
            if numlibrosautor == 0:
                print("Autor no encontrado en la lista ")
            else:
                print(f"Autor encontrado, tenemos {numlibrosautor} libros de el los cuales son: ")
                for libro in librosautor:
                    print(libro)
        case _:
            print("Error no ha ingresado un numero entre 1 y 2")
            
# Función para mostrar los libros (solo disponibles o todos) 
def mostrar_libros():
     num = int(input("Deseas ver  1 : Solo los libros disponibles, 2 : Todos los libros "))
     if num == 1:
         for libro in libros:
             if libro[3] > 0: # si el numero de libros disponible es mayor a uno el libro esta disponible
                 print(libro)
     elif num == 2:
        for libro in libros:
            print(libro)
     else:
        print("Error no ha ingresado un numero entre 1 y 2")

# Función para añadir un nuevo usuario
def anadir_usuario():
    tab = []
    tab.append(input("Ingresa el nombre completo del usuario: "))
    tab.append(int(input("Ingresar el codigo del usuario: ")))
    tab.append(input("Ingresa el correo del usuario: "))
    usuarios.append(tab)
    prestos[tab[1]] = []
    return tab


# Función para editar un usuario
def editar_usuario():
    codigo = int(input("Ingresar el codigo del usuario que quieres editar: "))
    for usuario in usuarios:
        if codigo == usuario[1]:
            while True: 
                num = int(input("Que quieres cambiar : 1 = Cambiar nombre / 2 = Cambiar el codigo de usuario  / 3 = Cambiar el correo: "))
                match num :
                    case 1:
                        usuario[0] = input("Ingresar el nuevo nombre para el usuario: ")
                        break
                    case 2:
                        usuario[1] = int(input("Ingresar el nuevo codigo para el usuario: "))
                        break
                    case 3:
                        usuario[2] = input("Ingresar el nuevo correo del usuario: ")
                        break
                    case _:
                        print("Error ingrese un numero entre 1 y 3 ")
            break   
    else : 
        print("Usuario no encontrado")

# Función para borrar un usuario con su codigo
def borrar_usuario():
    codigo = int(input("Ingresar el codigo del usuario que quieres borrar: "))
    for usuario in usuarios:
        if codigo == usuario[1]:
            usuarios.remove(usuario)
            print(f"El usuario: {usuario} se acaba de borrar ")
            break
    else:
        print("Usuario no encontrado en la lista")

# Función para buscar un usuario con su codigo
def buscar_usuario():
        codigo = int(input("Ingresar el codigo del usuario que deseas buscar: "))
        for usuario in usuarios:
            if codigo == usuario[1]:
                print(f"Usuario encontrado: {usuario}")
                return True, usuario
        else:
            print("Usuario no encontrado en la lista ")
            return False
            
# Función para mostrar todos los usuarios
def mostrar_usuarios():
    for usuario in usuarios:
        print(usuario)
        
# Función para añadir un nuevo presto
def anadir_presto():
    bool1 , user = buscar_usuario() #En primer lugar buscamos el usuario
    if bool1:
        print("Usa la funcion buscar_libro con la opcion 1 !! ") 
        bool2, book = buscar_libro() # Despues buscamos el libro
        if bool2:           
            if book[3] >0 : #El libro debe ser disponible para permitir el presto
                if len(prestos[user[1]]) <= 3: #Un usuario no puede pedir mas de 4 libros 
                    prestos[user[1]].append(book[0])
                    print(f"Presto anadido : el usario {user} tiene el libro {book}")
                    book[3] -= 1 # Cambiamos el numero de libros disponibles 
                else:
                    print(" El usuario ya tiene 4 libros, no puede pedir mas ahora ")
            else:
                print(" No hay mas de ese libro")
    else:
        print("Ese usuario no es registrado")

# Función para devolver un libro
def devolver_libro():
    codigo = int(input("Ingresar el codigo del usuario que va a devolver un libro: "))
    if codigo in prestos:
        if len(prestos[codigo]) == 0:
            print("El usuario no tiene libros prestados.")
            return
        print("Libros que tiene prestados el usuario:")
        for i, libro in enumerate(prestos[codigo], start=1):
            print(f"{i}. {libro}")
        num = int(input("Ingrese el numero del libro que desea devolver: "))
        if 1 <= num <= len(prestos[codigo]):
            nombre_libro = prestos[codigo][num - 1]
            prestos[codigo].remove(nombre_libro)
            # aumentar la cantidad disponible del libro devuelto
            for libro in libros:
                if libro[0].lower() == nombre_libro.lower():
                    libro[3] += 1
                    break
            print(f"El libro '{nombre_libro}' fue devuelto correctamente.")
        else:
            print("Numero no valido.")
    else:
        print("Usuario no encontrado o no tiene prestamos registrados.")


                
                    
while True:
    print("-- Menu Biblioteca --")
    print("\n")
    print("1 : Añadir un libro")
    print("2 : Editar un libro")
    print("3 : Borrar un libro")
    print("4 : Buscar un libro")
    print("5 : Mostrar los libros")
    print("6 : Añadir un usuario")
    print("7 : Editar un usuario")
    print("8 : Borrar un usuario")
    print("9 : Buscar un usuario")
    print("10 : Mostrar los usuarios")
    print("11 : Añadir un libro prestado")
    print("12 : Devolver un libro")
    print("13 : Salir del menu")
    opcion = int(input("Ingrese una opcion "))
    
    match opcion :
        case 1:
            libro1 = anadir_libro()
            print(f" El libro {libro1} fue anadido con exito")
        case 2:
            editar_libro()
        case 3:
            borrar_libro()
        case 4:
            buscar_libro()
        case 5:
            mostrar_libros()
        case 6:
            usuario1 = anadir_usuario()
            print(f" El usuario {usuario1} fue anadido con exito")
        case 7:
            editar_usuario()
        case 8:
            borrar_usuario()
        case 9:
            buscar_usuario()
        case 10:
            mostrar_usuarios()
        case 11:
            anadir_presto()
        case 12:
            devolver_libro()
        case 13:
            print("Ciao, Hasta luego")
            break
            
            
            
            
            
