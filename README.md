# 📝 Task Manager API

Pequeña API REST para la gestión de tareas, creada con **Flask** y contenida usando **Docker** y **Docker Compose**. Este proyecto fue diseñado como una práctica para contenerización de servicios y despliegue local.

---

## 🚀 Tecnologías utilizadas

- Python 3.10
- Flask 2.3.2
- Docker
- Docker Compose

---

## 📁 Estructura del proyecto

```
Lista1/
├── app.py                  # Aplicación principal con Flask
├── requirements.txt        # Dependencias de Python
├── Dockerfile              # Imagen base y comandos de construcción
├── docker-compose.yml      # Orquestación del contenedor
└── README.md               # Este archivo
```

---

## ⚙️ Cómo usar

### 1. Clona o descarga el proyecto

```bash
git clone https://github.com/tu-usuario/Lista1.git
cd Lista1
```

### 2. Construye y ejecuta con Docker Compose

```bash
docker-compose up --build
```

Esto levantará la API en `http://localhost:5000`.

---

## 📡 Endpoints disponibles

### `GET /tasks`
Obtiene la lista de tareas.

```bash
curl http://localhost:5000/tasks
```

---

### `POST /tasks`
Agrega una nueva tarea.

```bash
curl -X POST http://localhost:5000/tasks \
     -H "Content-Type: application/json" \
     -d "{\"nombre\": \"Estudiar Docker\", \"estado\": \"pendiente\"}"
```

---

## 🧼 Detener la aplicación

```bash
docker-compose down
```

---

## 📌 Notas

- No hay base de datos; las tareas se almacenan en memoria (solo mientras se ejecuta el contenedor).
- Puedes extender fácilmente este proyecto para persistencia con SQLite, PostgreSQL, MongoDB, etc.

---

## 👨‍💻 Autor

Desarrollado por [Tu Nombre o Usuario](https://github.com/tu-usuario)
