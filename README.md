# LAB3 - Sistema de Gestión de Eventos

Este proyecto implementa un sistema CRUD completo para gestionar eventos académicos y registrar participantes, utilizando SQLAlchemy como ORM, PostgreSQL como base de datos y Streamlit como interfaz web.

## Funcionalidades

- Crear eventos con múltiples participantes.
- Asignar automáticamente estado "Pendiente" al crear.
- Editar la información del evento y el estado individual de cada participante.
- Eliminar eventos junto con sus inscripciones.
- Visualizar un resumen de eventos desde una vista (`eventos_resumen`).

---

## 📦 Tecnologías utilizadas

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [Plotly](https://plotly.com/python/)
- [FPDF](https://py-pdf.github.io/fpdf2/)

---

## 📁 Estructura del proyecto

```plaintext
├── app.py                         # Punto de entrada con menú lateral
├── views/                         # Vistas de cada acción CRUD
│ ├── crear_evento.py
│ ├── ver_eventos.py
│ ├── editar_evento.py
│ └── eliminar_evento.py
├── models/                       # Modelos ORM
│ ├── evento.py
│ ├── participante.py
│ ├── evento_participante.py
│ ├── tipo_evento.py
│ └── estado_inscripcion.py
├── utils/
│ └── crud_eventos.py             # Lógica de base de datos con SQLAlchemy
├── database/
│ ├── 1_ddl.sql                    # Script de creación de tablas y VIEW
│ └── 2_data.sql                   # Datos de prueba 
├── Dockerfile                     # Imagen de la app
├── docker-compose.yml             # Define los servicios (app y base de datos)

```

## Requisitos

- Docker Desktop
- Navegador web (Chrome, Edge, Firefox)

---

## ⚙️ Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone repo
```

### 2. Ejecuta con Docker

```bash
docker-compose up --build
```

### 3. Abre la aplicación en el navegador 
```bash
http://localhost:8502
```

Servidor disponible en:  
📍 \`http://localhost:8502\`

---

## Vista (VIEW)
La vista eventos_resumen muestra un resumen de eventos, su tipo y cantidad de participantes confirmados.
Se utiliza exclusivamente para poblar el índice de eventos (pantalla “Ver Eventos”).

---

## 👩‍💻 Autores

Vianka Castro - 23201
Ricardo Godínez - 23247
