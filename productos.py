
import re
import unicodedata

def normalizar(texto):
    texto = unicodedata.normalize(
        "NFKD", str(texto)
    )
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    ).lower()

def reconocer_producto(nombre):
    texto = normalizar(nombre)
    palabras = set(re.findall(r"[a-z0-9]+", texto))

    medidas = re.findall(
        r"\b(\d+(?:[.,]\d+)?)\s*(ml|g)\b",
        texto
    )

    tamano = None
    if len(medidas) == 1:
        cantidad, unidad = medidas[0]
        tamano = (
            float(cantidad.replace(",", ".")),
            unidad
        )

    tonos = [
        t for t in ["light", "medium", "dark", "bronze"]
        if t in palabras
    ]

    if palabras.intersection(
        {"refill", "repuesto", "recarga"}
    ):
        envase = "Refill"
    elif palabras.intersection(
        {"kit", "pack", "combo"}
    ):
        envase = "Kit"
    else:
        envase = "No confirmado"

    return {
        "nombre": nombre,
        "tamano": tamano,
        "tono": tonos[0] if len(tonos) == 1 else None,
        "envase": envase
    }
