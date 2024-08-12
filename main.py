import json

####################
##json de ventas

def archivo():
    miJSON=[]
    with open('./ventas.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def archivoGuardadito(miData):
    with open("./ventas.json","w") as outfile:
        json.dump(miData,outfile)

####################
##json de pacientes 
def archivoPacientes():
    miJSON=[]
    with open('./pacientes.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoPacientes(miData):
    with open("./pacientes.json","w") as outfile:
        json.dump(miData,outfile)

####################
##json de proovedores
def archivoProovedores():
    miJSON=[]
    with open('./proovedores.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardadoProovedores(miData):
    with open("./proovedores.json","w") as outfile:
        json.dump(miData,outfile)

####################
##json de medicamentos
def archivoMedicamentos():
    miJSON=[]
    with open('./medicamentos.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoMedicamentos(miData):
    with open("./medicamentos.json","w") as outfile:
        json.dump(miData,outfile)

####################
##json de empleados 
def archivoEmpleados():
    miJSON=[]
    with open('./empleados.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoEmpleados(miData):
    with open("./empleados.json","w") as outfile:
        json.dump(miData,outfile)

##################
##json de compras
def archivoCompras():
    miJSON=[]
    with open('./compras.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoCompras(miData):
    with open("./compras.json","w") as outfile:
        json.dump(miData,outfile)

def GuardarVentas():
    try:
        with open("ventas.json","r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []
    
def guardarcompras():
    try:
        with open("compras.json","r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []

transacciones= GuardarVentas()
comprass= guardarcompras()

print("----------------------")
print("BIENVENIDO LA FARMACIA")
print("----------------------")
print("")
print("que gestion desea realizar")
print("1. ventas")
print("2. compras")
queopcion=input("Que opcion desea realizar :")

booleano=True
while booleano:
    if queopcion=="1":
        print("---------------------------------")
        print("BIENVENIDO A LA SECCION DE VENTAS")
        print("---------------------------------")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        queFecha=input("En que fecha se realizo la venta: ")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        infoPaciente=input("cual es el nombre de el paciente: ")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        direccionPaciente=input("Cual es la direccion de el paciente: ")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("--EMPLEADOS--")
        atendio=archivoEmpleados()
        for i in atendio:
            print("|NOMBRE: ",i["nombre"])
        print("")
        empleado=input("Que empleado atendio al cliente: ")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("--MEDICAMENTOS--")
        Nombremedi=archivoMedicamentos()
        for i in Nombremedi:
            print("|NOMBRE: ",i["nombre"] )
        print("")
        nombreMedicamento=input("ingresa el nombre de el medicamento: ")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        cantidadMedicamento=input("que cantidad va a llevar: ")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        precioMedicamento=input("cual es el costo de la compra: ")
        print("")
        venta={
            "fecha": queFecha,
            "paciente": infoPaciente,
            "empleado": empleado,
            "medicamento":{
                "nombre":nombreMedicamento,
                "cantidad":cantidadMedicamento,
                "precio": precioMedicamento
            }
        }
        transacciones.append(venta)
        archivoGuardadito(transacciones)
        print("------------------------------------")
        print("------la venta se ha realizado------")
        print("------------------------------------")
        booleano=False

    if queopcion=="2":
        print("----------------------------------")
        print("BIENVENIDO A LA SECCION DE COMPRAS")
        print("----------------------------------")
        print("")
        jsoonCompras=archivoCompras()
        print("°°°°°°°°°°°°°°°°°°°°°")
        fechaCompra=input("En que fecha se realizo la compra: ")
        print("°°°°°°°°°°°°°°°°°°°°°")
        jsonproovedores=archivoProovedores()
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("--PROVEEDORES--")
        for i in jsonproovedores:
            print("|NOMBRE: ",i["nombre"])
            print("|CONTACTO: ",i["contacto"])
            print("")
        queProovedor=input("Que proovedor atendio la compra: ")
        print("°°°°°°°°°°°°°°°°°°°°°")
        contactoProovedor=("Cual es el numero de el proovedor: ")
        print("°°°°°°°°°°°°°°°°°°°°°")
        Nombremedi=archivoMedicamentos()
        print("°°°°°°°°°°°°°°°°°°°°°")
        print("--MEDICAMENTOS--")
        for i in Nombremedi:
            print("|NOMBRE : ",i["nombre"])
        print("")
        queMedicamento=input("cual es el nombre del medicamento: ")
        print("°°°°°°°°°°°°°°°°°°°°°")
        queCantidad=input("Que cantidad del producto llevo :")
        print("°°°°°°°°°°°°°°°°°°°°°")
        quePrecio=input("De que precio fue la compra: ")
        print("")
        compra={
            "fechaCompra": fechaCompra,
            "proveedor"
                "nombre": queProovedor,
                "contacto": contactoProovedor,
            "medicamentosComprados"
                    "nombreMedicamento": queMedicamento,
                    "cantidadComprada": queCantidad,
                    "precioCompra": quePrecio
        }
        comprass.append(compra)
        archivoGuardadito(comprass)
        print("------------------------------------")
        print("------la compra se ha realizado------")
        print("------------------------------------")
        print("")
        print("------------------------------------")
        print("1. VOLVER AL MENU DE INICIO")
        print("2. SALIR DEL PROGRAMA")
        deseaSalir=input("Escoge una opcion: ")
        booleano=False