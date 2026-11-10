
import streamlit as st
import pandas as pd

from productos import reconocer_producto
from comparador import comparar
from alertas import evaluar_alerta

st.set_page_config(
    page_title="App Skincare Demo",
    page_icon="💜"
)

st.title("💜 Comparador de belleza")
st.info("Prototipo con tiendas y precios ficticios.")

catalogo = [
    ("Tienda A", "Crema Brisa Suave 50 ml", 54000),
    ("Tienda B", "Crema Brisa Suave 50 ml", 62000),
    ("Tienda A", "Serum Aurora Calm 30 ml", 75000),
    ("Tienda B", "Serum Aurora Calm 30 ml", 89000)
]

producto = st.selectbox(
    "Selecciona un producto",
    [
        "Crema Brisa Suave 50 ml",
        "Serum Aurora Calm 30 ml"
    ]
)

objetivo = st.number_input(
    "Precio objetivo de prueba (COP)",
    min_value=1,
    value=70000
)

if st.button("Comparar precios"):

    st.write("**Producto:**", producto)
    st.write(
        "**Reconocimiento:**",
        reconocer_producto(producto)
    )

    resultados = []

    for tienda, nombre, precio in catalogo:
        estado = comparar(producto, nombre)

        if estado.startswith("Candidato comparable"):
            resultados.append({
                "Tienda": tienda,
                "Producto": nombre,
                "Precio COP": precio
            })

    if resultados:
        tabla = pd.DataFrame(resultados)
        tabla = tabla.sort_values("Precio COP")

        st.subheader("Comparación")
        st.dataframe(tabla, hide_index=True)

        mejor = tabla.iloc[0]

        st.success(
            f"Menor precio simulado: "
            f"${mejor['Precio COP']:,.0f}"
        )

        alerta = evaluar_alerta(
            producto,
            float(mejor["Precio COP"]),
            float(objetivo)
        )

        st.info(alerta["Mensaje"])

    else:
        st.warning("No hay resultados comparables.")

st.caption(
    "Demostración sin precios reales, "
    "sin compras ni conexiones a tiendas."
)
