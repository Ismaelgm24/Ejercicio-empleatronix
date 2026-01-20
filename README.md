# EMPLEATRONIX

Aplicación web interactiva para visualizar y analizar datos de empleados, desarrollada con Streamlit y Docker.

## Descripción
EMPLEATRONIX permite cargar, visualizar y analizar información de empleados desde un archivo CSV. Incluye una tabla interactiva y una gráfica de barras personalizable, con opciones para mostrar/ocultar nombres y sueldos, y elegir el color de las barras. El pie de página muestra el nombre del autor.

## Características
- Visualización de datos de empleados desde `BD/employees.csv`.
- Tabla interactiva con todos los campos.
- Gráfica de barras horizontal personalizable:
  - Cambia el color de las barras.
  - Muestra/oculta nombres y sueldos en la gráfica.
- Pie de página con el nombre del autor.
- Contenerización con Docker para fácil despliegue.

## Estructura del proyecto
```
├── BD/
│   └── employees.csv
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Requisitos
- Docker

## Instrucciones de uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/empleatronix.git
cd empleatronix
```

### 2. Construir y ejecutar con Docker
```bash
docker-compose up --build
```
La aplicación estará disponible en [http://localhost:8501](http://localhost:8501)

### 3. Personalización
- Para cambiar los datos, edita el archivo `BD/employees.csv`.
- Para modificar la visualización, edita `streamlit_app.py`.

## Link de la app
https://ejercicio-empleatronix-kqsnmdx8e4pyntsb7srgjc.streamlit.app/

## Autor
© Ismael Guerrero Martín

---

¡Disfruta visualizando tus datos de empleados con EMPLEATRONIX!
