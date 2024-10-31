import streamlit as st

# Función para dividir el archivo en fragmentos
def dividir_archivo_por_palabras(file_content, cantidad_palabras):
    # Dividir el contenido en palabras
    palabras = file_content.split()
    fragmentos = []
    
    # Crear fragmentos según la cantidad de palabras
    for i in range(0, len(palabras), cantidad_palabras):
        fragmento = ' '.join(palabras[i:i + cantidad_palabras])
        fragmentos.append(fragmento)
    
    return fragmentos

# Interfaz en Streamlit
st.title("Divisor de Archivos .txt en Fragmentos")

# Cargar archivo .txt
archivo_subido = st.file_uploader("Sube un archivo .txt", type="txt")
cantidad_palabras = st.number_input("Introduce la cantidad máxima de palabras por fragmento", min_value=1)

if archivo_subido and cantidad_palabras:
    # Leer contenido del archivo
    contenido = archivo_subido.read().decode("utf-8")
    fragmentos = dividir_archivo_por_palabras(contenido, cantidad_palabras)

    # Descargar los fragmentos generados
    for idx, fragmento in enumerate(fragmentos, 1):
        fragmento_nombre = f"{idx}.txt"
        st.download_button(
            label=f"Descargar {fragmento_nombre}",
            data=fragmento,
            file_name=fragmento_nombre,
            mime="text/plain"
        )
