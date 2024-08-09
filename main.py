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
        print("")
        jsoonVentas=archivo()
        for i in jsoonVentas:
            queFecha=input("en que fecha se realizo la venta: ")
            archivoGuardadito(queFecha)
        jsoonVentas2=archivoPacientes()
        for i in jsoonVentas2:
            queNombre=input("que nombre tiene el paciente: ")
            queDireccion=input("cual es la dirrecion de el cliente")
            GuardaditoPacientes(queNombre,queDireccion)
        jsoonVentas3=archivoEmpleados()
        for i in jsoonVentas3:
            queProovedor=input("cual es el nombre de el proovedor: ")
            queCargo=input("que cargo tenia el proovedor: ")
            GuardaditoEmpleados(queProovedor,queCargo)
        jsoonVentas4=archivoMedicamentos()
        for i in jsoonVentas4:
            queProducto=input("cual es el nombre de el producto: ")
            queCantidad=input("que cantidad tiene el producto: ")
            quePrecio=input("que precio tiene la venta: ")
            GuardaditoMedicamentos(queProducto,queCantidad,quePrecio)
        booleano=False
    if queopcion=="2":
        print("----------------------------------")
        print("BIENVENIDO A LA SECCION DE COMPRAS")
        print("----------------------------------")
        print("")
        jsoonCompras=archivoCompras()
        for i in jsoonCompras:
            queFecha2=input("en que fecha se realizo la venta: ")
            archivoGuardadito(queFecha2)
        jsoonCompras2=archivoProovedores()
        for i in jsoonCompras2:
            queProovedor2=input("cual es el nombre de el proovedor: ")
            archivoGuardadito(queProovedor2)
        for i in jsoonVentas3:
            queProovedor2=input("cual es el nombre de el proovedor: ")
            queCargo2=input("que cargo tenia el proovedor: ")
            GuardaditoEmpleados(queProovedor2,queCargo2)
        jsoonCompras4=archivoCompras()
        for i in jsoonCompras4:
            queNombre3=input("que nombre tiene el producto: ")
            queCantidad3=input("que cantidad de productos llevo: ")
            quePrecio3=input("que precio tuvo la compra: ")
            GuardaditoCompras(queNombre3,queCantidad3,quePrecio3)
            booleano=False
        

        

