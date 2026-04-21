from analizador import (
    calcular_total,
    calcular_promedio,
    calcular_gasto_mayor,
    calcular_categoria_mayor,
)


def test_calcular_total():
    matriz = [
        ["fecha", "categoria", "descripcion", "monto"],
        ["2026-01-01", "comida", "supermercado", "1000"],
        ["2026-01-02", "transporte", "SUBE", "500"],
    ]
    assert calcular_total(matriz) == 1500


def test_calcular_total_vacio():
    matriz = [["fecha", "categoria", "descripcion", "monto"]]
    assert calcular_total(matriz) == 0


def test_calcular_promedio():
    matriz = [
        ["fecha", "categoria", "descripcion", "monto"],
        ["2026-01-01", "comida", "supermercado", "1000"],
        ["2026-01-02", "transporte", "SUBE", "500"],
    ]
    assert calcular_promedio(matriz) == 750


def test_calcular_gasto_mayor():
    matriz = [
        ["fecha", "categoria", "descripcion", "monto"],
        ["2026-01-01", "comida", "supermercado", "1000"],
        ["2026-01-02", "transporte", "SUBE", "500"],
    ]
    assert calcular_gasto_mayor(matriz) == (1000, "supermercado")


def test_calcular_categoria_mayor():
    matriz = [
        ["fecha", "categoria", "descripcion", "monto"],
        ["2026-01-01", "comida", "supermercado", "1000"],
        ["2026-01-02", "transporte", "SUBE", "500"],
    ]
    assert calcular_categoria_mayor(matriz) == "comida"
