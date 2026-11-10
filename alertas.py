
def evaluar_alerta(producto, precio_actual, precio_objetivo):

    if precio_actual <= 0 or precio_objetivo <= 0:
        raise ValueError("Los precios deben ser positivos")

    diferencia = precio_actual - precio_objetivo

    if diferencia <= 0:
        estado = "Objetivo alcanzado"
        mensaje = (
            f"¡El producto alcanzó tu objetivo! "
            f"Está ${abs(diferencia):,.0f} "
            f"por debajo o igual al valor deseado."
        )
    else:
        estado = "En seguimiento"
        mensaje = (
            f"El precio debe bajar "
            f"${diferencia:,.0f} para alcanzar tu objetivo."
        )

    return {
        "Producto": producto,
        "Precio actual": precio_actual,
        "Precio objetivo": precio_objetivo,
        "Estado": estado,
        "Mensaje": mensaje
    }
