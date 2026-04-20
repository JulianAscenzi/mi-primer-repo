def leer_csv(archivo):
    matriz = []
    with open(archivo, "r") as f:
        lineas = f.readlines()
        for linea in lineas:
            matriz.append((linea.strip()).split(","))

    return matriz

def calcular_total(matriz):
    gasto_total = 0
    for fila in matriz[1:]:
        gasto = int(fila[3])
        gasto_total += gasto
    return gasto_total

def calcular_promedio(matriz):
    return calcular_total(matriz)/ (len(matriz)-1)

def calcular_gasto_mayor(matriz):
    max = 0
    descripcion_max = ""
    for fila in matriz[1:]:
        gasto = int(fila[3])
        descripcion = fila[2]
        if gasto > max:
            max = gasto
            descripcion_max = descripcion
    return (max, descripcion_max)

def calcular_categoria_mayor(matriz):
    categorias = {}
    maximo = 0
    res = ""
    for fila in matriz[1:]:
        categoria = fila[1]
        gasto = int(fila[3])
        if categoria not in categorias:
            categorias[categoria] = gasto
        else:
            categorias[categoria] += gasto
        if categorias[categoria] > maximo:
            res = categoria
            maximo = categorias[categoria]
    return res

def main():
    matriz = leer_csv("gastos.csv")
    print("Total gastado: " + "$" + str(calcular_total(matriz)))
    print("Promedio por gasto: " + "$" + str(calcular_promedio(matriz)))
    gasto_mayor = calcular_gasto_mayor(matriz)
    print("Gasto mayor: " + gasto_mayor[1] + " " + "(" + "$" + str(gasto_mayor[0]) + ")")
    print("Categoría con más gastos: " + calcular_categoria_mayor(matriz))
    
if __name__ == "__main__":
    main()