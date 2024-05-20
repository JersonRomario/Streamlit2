import streamlit as st
import pandas as pd
import re

def read_file(file):
    lines = file.read().decode("utf-8").splitlines()
    data = []
    for line in lines:
        parts = re.split(r',\s*|\s*:\s*', line)
        estudiante = parts[0]
        matematicas = int(parts[2])
        fisica = int(parts[4])
        quimica = int(parts[6])
        data.append([estudiante, matematicas, fisica, quimica])
    df = pd.DataFrame(data, columns=["Estudiante", "Matematicas", "Fisica", "Quimica"])
    return df

def calculate_averages(data):
    data['Promedio'] = data[['Matematicas', 'Fisica', 'Quimica']].mean(axis=1)
    return data[['Estudiante', 'Promedio']]

def save_averages(averages):
    averages.to_csv("promedios_estudiantes.csv", index=False)

def main():
    st.title("Cálculo de Promedios de Estudiantes")

    uploaded_file = st.file_uploader("Sube tu archivo de texto", type=["txt"])

    if uploaded_file is not None:
        data = read_file(uploaded_file)
        st.write("Datos cargados:")
        st.dataframe(data)

        averages = calculate_averages(data)
        st.write("Promedios de los estudiantes:")
        st.dataframe(averages)

        save_averages_button = st.button("Guardar promedios en archivo")

        if save_averages_button:
            save_averages(averages)
            st.success("Archivo guardado con éxito como 'promedios_estudiantes.csv'.")

if __name__ == "__main__":
    main()
