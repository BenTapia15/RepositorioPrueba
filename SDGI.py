nombresProductos=[]
stocksProductos=[]
preciosProductos=[]
listaProductos=[]
#producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
#el codigo tiene que tener 3 validaciones 
opcion="0"
"""
 Cambiar las listas para crear el producto por un diccionario []
 Agregar un codigo al diccionario de productos []
 Agregar una lista para almacenar los diccionarios de producto []
 Modificar las funciones para que utilizen la nueva estructura de diccionario []
 Agregar las funciones faltantes:
    Actualizar cantidad/precio []
    Mostrar inventario completo []
    Eliminar producto []
""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
def ValidarCodigo(codigo):
    #codigo="Diego"
    ContadorMayusculas=0
    ContadorNumeros=0
    for l in codigo:
        if l.isupper:
            ContadorMayusculas+=1
        if l.isnumeric:
            ContadorNumeros=+1
    if ContadorMayusculas<2:
        print ("*el codigo debe tener almenos 2 mayusculas")
        return False
    elif ContadorNumeros==0:
        print ("el codigo debe tener al menos un numero")
        return False
    elif len(codigo) < 5:
        print ("El codigo debe tener al menos 5 caracteres")
        return False
    else:
        return True

def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    while True:
        codigo=input("ingrese el codigo para el producto ")
        if ValidarCodigo(codigo)==True:
            print ("codigo correcto!")
            break
        else:
            print ("El codigo es incorrecto. debe volver a ingresar")
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
                
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")

def guardarProducto(nombre,precio,stock):
    """"
    if nombre not in nombresProductos:
        nombresProductos.append(nombre)
        preciosProductos.append(precio)
        stocksProductos.append(stock)
        print("Se guardado correctamente el producto")
    """
    for producto in listaProductos:
        if codigo==producto["codigo"]:
            print ("Ese producto ya fue registrado")
def buscarProducto(nombre):
    if nombre in nombresProductos:
        indice= nombresProductos.index(nombre)
        nombre=nombresProductos[indice]
        precio=preciosProductos[indice]
        stock=stocksProductos[indice]
        print("-"*60)
        print(f"Nombre: {nombre} \t Precio: ${precio} \t Stock: {stock} unidades")
        print("-"*60)
        #return [nombre,precio,stock]
            
    else:
        print("No existe un producto con ese nombre")

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")


    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

