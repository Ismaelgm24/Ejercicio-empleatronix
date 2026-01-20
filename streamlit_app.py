import streamlit as st
import pandas as pd
import altair as alt
# Título principal
st.markdown("<h1 style='font-size: 48px; font-weight: bold;'>EMPLEATRONIX</h1>", unsafe_allow_html=True)

# Descripción
st.write("Todos los datos sobre los empleados en una aplicación.")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("BD/employees.csv")

df = load_data()

# Mostrar tabla de empleados
st.dataframe(df, use_container_width=True)

st.markdown("---")

# Opciones de visualización
col1, col2, col3 = st.columns([2, 2, 6])
with col1:
    color = st.color_picker("Elige un color para las barras", "#20b9e3")
with col2:
    show_name = st.toggle("Mostrar el nombre", value=True)
with col3:
    show_salary = st.toggle("Mostrar sueldo en la barra", value=False)



# Preparar datos para la gráfica
bar_data = df[['full name', 'salary']].copy()

# Crear gráfica con Altair para personalizar etiquetas
if not show_name:
    chart = alt.Chart(bar_data).mark_bar(color=color).encode(
        y=alt.Y('full name:N', title=None, axis=alt.Axis(labels=False, ticks=True)),
        x=alt.X('salary:Q', title=None)
    )
else:
    chart = alt.Chart(bar_data).mark_bar(color=color).encode(
        y=alt.Y('full name:N', title=None, sort='-x'),
        x=alt.X('salary:Q', title=None)
    )

# Añadir etiquetas de sueldo si corresponde
if show_salary:
    text = alt.Chart(bar_data).mark_text(
        align='left',
        baseline='middle',
        dx=5  # desplazamiento horizontal
    ).encode(
        y=alt.Y('full name:N', sort='-x'),
        x=alt.X('salary:Q'),
        text=alt.Text('salary:Q')
    )
    chart = chart + text

st.altair_chart(chart, use_container_width=True)

# Pie de página
st.markdown('<div style="text-align: left; color: gray; font-size: 15px; margin-top: 40px;">© Ismael Guerrero Martín</div>', unsafe_allow_html=True)
