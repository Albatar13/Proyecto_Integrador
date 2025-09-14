libros = []

def anadir_libro():
    tab = []
    tab.append(input("Ingresar el nombre del libro"))
    tab.append(input("Ingresar el nombre del autor"))
    tab.append(input("Ingresar la fecha de publicacion"))
    tab.append(input("Ingresar el  numero de libros disponible"))
    print(tab)
    libros.append(tab)

def editar_libro():
    nombre = input("Ingresar el nombre del libro que quieres editar")
    for libro in libros:
        if nombre == libro[0]:
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
                        libro[2] = input("Ingresar la nueva fecha")
                        break
                    case 4: 
                        libro[3] = input("Ingresar el nuevo numero de libros disponible")
                        break
                    case _:
                        print("Error ingrese un numero entre 1 y 4 ")
            break
    else : 
        print("Livre no encontrado en la lista")
        
