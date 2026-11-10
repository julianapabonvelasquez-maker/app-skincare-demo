
from productos import reconocer_producto, normalizar
import re

def palabras_base(nombre):
    texto = normalizar(nombre)
    palabras = set(re.findall(r"[a-z0-9]+", texto))

    excluir = {
        "isdin", "isdinceutics", "ml", "g",
        "light", "medium", "dark", "bronze",
        "refill", "repuesto", "recarga",
        "kit", "pack", "combo", "serum",
        "antimanchas", "contorno", "ojos"
    }

    return {
        p for p in palabras
        if p not in excluir and not p.isdigit()
    }

def comparar(referencia, candidato):
    a = reconocer_producto(referencia)
    b = reconocer_producto(candidato)

    # Identificar la familia
    if palabras_base(referencia) != palabras_base(candidato):
        return "No comparable: producto diferente"

    # Verificar tamaño
    if a["tamano"] is None or b["tamano"] is None:
        return "Revisión manual: tamaño desconocido"

    if a["tamano"] != b["tamano"]:
        return "No comparable: tamaño diferente"

    # Verificar tono
    if a["tono"] != b["tono"]:
        return "Revisión manual: tono diferente o desconocido"

    # Excluir tipos de presentación diferentes
    if a["envase"] != b["envase"]:
        return "No comparable: presentación diferente"

    if a["envase"] == "No confirmado":
        return "Candidato comparable: verificar envase"

    return "Candidato comparable: verificar identidad"
