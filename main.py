usuarios = [] 
def anadir_libro():
    tab = []
    tab.append(input("Ingresar el nombre del libro: "))
    tab.append(input("Ingresar el nombre del autor: "))
    tab.append(int(input("Ingresar la fecha de publicacion: ")))
    tab.append(int(input("Ingresar el  numero de libros disponible: ")))
    print(tab)
    libros.append(tab)

def editar_libro():
    nombre = input("Ingresar el nombre del libro que quieres editar")
    for libro in libros:
        if nombre.lower() == libro[0].lower():
            while True: 
                num = int(input("Que quieres cambiar : 1 = Cambiar nombre / 2 = Cambiar autor / 3 = Cambiar fecha publicacion / 4= Cambiar numero disponible"))
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

def borrar_libro():
    nombre = input("Ingresar el nombre del libro que quieres borrar")
    for libro in libros:
        if nombre.lower() == libro[0].lower():
            libros.remove(libro)
            break
    else:
        print("Libro no encontrado en la lista ")
        
def buscar_libro():
    num = int(input("Quieres buscar con el nombre : ingresa 1 o con el autor : ingresa 2"))
    match num:
        case 1:
            nombre = input("Ingresar el nombre del libro que quieres buscar")
            for libro in libros:
                if nombre.lower() == libro[0].lower():
                    print("Libro encontrado sus informaciones son :")
                    print(libro)
                    break
            else:
                print("Libro no encontrado en la lista ")
        case 2:
            autor = input("Ingresar el nombre del autor que quieres buscar")
            numlibrosautor = 0
            librosautor = []
            for libro in libros:
                if autor.lower() == libro[1].lower():
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
def anadir_usuario():
    tab = []
    tab.append(input("Ingresa el nombre completo del usuario: "))
    tab.append(int(input("Ingresar el codigo del usuario: ")))
    print(tab)
    usuarios.append(tab)
    

            
                
                    
