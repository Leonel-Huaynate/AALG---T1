class Puestos:
    def __init__(self,codigo,descripcion,areaSoli,plazas,sueldo):
        self.codigo=codigo
        self.descripcion=descripcion
        self.areaSoli=areaSoli
        self.plazas=plazas
        self.sueldo=sueldo
    def __str__(self):
        return f"Cod:{self.codigo} | {self.descripcion} | Area:{self.areaSolicitante} | Plazas:{self.plazasRequeridas} | Sueldo:{self.sueldo}"
    def total(self):
        return self.plazas*self.sueldo
    

def validarString(txt):
    return len(txt)>=3

def validarNum(num):
    return num>0

def AgregarPuesto(lista):
    codigo=int(input("Ingrese el codigo del puesto :"))
    descripcion=input("Ingrese la descripcion del puesto :")
    areaSoli=input("Ingrese la area que Solicita el puesto :")
    plazas=int(input("Ingrese las plazas requeridas por el puesto :"))
    sueldo=float(input("Ingrese el sueldo del puesto : "))

    if not (validarNum(codigo) and validarString(descripcion) and validarString(areaSoli) and validarNum(plazas) and validarNum(sueldo)):
        return print("Ingrese datos validos")
    
    for p in lista:
        if(p.codigo==codigo or p.descripcion or p.areaSoli==areaSoli):
            return print("Ya hay un puesto de trabajo igual")

    list.append(Puestos(codigo,descripcion,areaSoli,plazas,sueldo))
    print("Se registro el puesto")

def Mostrar(lista):
    for p in list:
        print(p)

def ordenar_Burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].codigo < lista[j+1].codigo:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def borraPuesto(lista):
    codigo = int(input("Codigo a borrar: "))
    ordenar_Burbuja(lista)

    for i, p in enumerate(lista):
        if p.codigo == codigo:
            del lista[i]
            print("Eliminado")
            return

    print("No encontrado")

def insercion_sueldo(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j].sueldo < actual.sueldo:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual

def buscaSueldo(lista):
    insercion_sueldo(lista)
    sueldo = float(input("Sueldo a buscar: "))

    izq=0
    der=len(lista)-1
    encontrado = -1

    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio].sueldo == sueldo:
            encontrado = medio
            break
        elif lista[medio].sueldo < sueldo:
            der = medio - 1
        else:
            izq = medio + 1

    if encontrado == -1:
        print("No encontrado")
        return

    # mostrar todos iguales
    i = encontrado
    while i >= 0 and lista[i].sueldo == sueldo:
        print(lista[i])
        i -= 1

    i = encontrado + 1
    while i < len(lista) and lista[i].sueldo == sueldo:
        print(lista[i])
        i += 1

def seleccion_total(lista):
    n = len(lista)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if lista[j].total() > lista[max_idx].total():
                max_idx = j
        lista[i], lista[max_idx] = lista[max_idx], lista[i]

def puestosAContratar(lista):
    monto = float(input("Monto total: "))
    seleccion_total(lista)

    suma = 0
    for p in lista:
        if suma + p.total() <= monto:
            print(p)
            suma += p.total()
        else:
            break

lista = []

while True:
    print("\n1.Agregar 2.Mostrar 3.Borrar 4.Buscar sueldo 5.Contratar 6.Salir")
    op = input("Opcion: ")

    if op == "1":
        AgregarPuesto(lista)
    elif op == "2":
        Mostrar(lista)
    elif op == "3":
        borraPuesto(lista)
    elif op == "4":
        buscaSueldo(lista)
    elif op == "5":
        puestosAContratar(lista)
    elif op == "6":
        break
    else:
        print("Opción inválida")