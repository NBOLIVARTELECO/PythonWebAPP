# Python Firebase Web App - Aplicación Educativa Interactiva

Esta es una aplicación web educativa construida con Flask y Firebase que incluye un sistema interactivo de enseñanza para aprender sobre desarrollo web con Python, Flask y Firebase Realtime Database.

## 🎯 Características

- **Gestión de Usuarios**: CRUD completo (Create, Read, Delete) de usuarios con Firebase
- **Tutorial Interactivo**: Guía paso a paso con 5 lecciones interactivas sobre Flask y Firebase
- **Ejercicios Prácticos**: 5 tipos de ejercicios interactivos para practicar conceptos
- **Interfaz Moderna**: Diseño responsive con Bootstrap 5 y Font Awesome
- **Sistema de Puntuación**: Seguimiento de progreso en los ejercicios

## 📋 Requisitos Previos

- Python 3.7 o superior
- Cuenta de Firebase (gratuita)
- Archivo de credenciales de Firebase

## 🚀 Instalación y Configuración

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar Firebase

1. Ve a la [Consola de Firebase](https://console.firebase.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Ve a **Project Settings > Service Accounts**
4. Genera una nueva clave privada (esto descargará un archivo JSON)
5. Renombra el archivo descargado a `testvscode.json` y colócalo en la raíz del proyecto

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=https://tu-proyecto.firebaseio.com
```

### 4. Ejecutar la aplicación

```bash
python main.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📁 Estructura del Proyecto

```
PythonWebAPP/
├── main.py                 # Aplicación principal Flask
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno (no incluir en git)
├── testvscode.json        # Credenciales de Firebase (no incluir en git)
├── README.md              # Este archivo
└── templates/
    ├── index.html         # Página principal con gestión de usuarios
    ├── tutorial.html      # Vista de tutorial interactivo
    └── practice.html      # Vista de ejercicios prácticos
```

## 🎓 Vistas de la Aplicación

### 1. Página Principal (`/`)
- Formulario para añadir nuevos usuarios
- Lista de usuarios registrados en Firebase
- Acceso rápido a Tutorial y Ejercicios

### 2. Tutorial Interactivo (`/tutorial`)
Guía paso a paso con 5 lecciones:

1. **Introducción**: Conceptos básicos de Flask y Firebase
2. **Rutas de Flask**: Explicación de las rutas y decoradores
3. **Integración con Firebase**: Operaciones CRUD con Firebase
4. **Templates HTML**: Sintaxis Jinja2 y renderizado
5. **Flujo Completo**: Proceso completo de principio a fin

**Características:**
- Navegación paso a paso con indicadores visuales
- Ejemplos interactivos y simulaciones
- Código con sintaxis destacada
- Animaciones y transiciones suaves

### 3. Ejercicios Prácticos (`/practice`)
5 tipos de ejercicios interactivos:

1. **Pregunta Múltiple**: Conceptos sobre Flask
2. **Completar Código**: Ejercicios de código de Firebase
3. **Verdadero/Falso**: Validación de conceptos
4. **Ordenar Pasos**: Drag & drop para ordenar el flujo
5. **Relacionar Conceptos**: Matching de conceptos con descripciones

**Características:**
- Sistema de puntuación en tiempo real
- Barra de progreso visual
- Retroalimentación inmediata
- Resumen final con resultados

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.2
- **Base de Datos**: Firebase Realtime Database
- **Frontend**: Bootstrap 5.3.0
- **Iconos**: Font Awesome 6.4.0
- **Autenticación**: Firebase Admin SDK 6.4.0
- **Variables de Entorno**: python-dotenv 1.0.1

## 📚 Conceptos Enseñados

- **Flask Framework**: Rutas, decoradores, renderizado de templates
- **Firebase Realtime Database**: Operaciones CRUD, estructura de datos
- **Jinja2 Templates**: Sintaxis, bucles, condicionales
- **HTTP Methods**: GET, POST, redirecciones
- **Arquitectura Web**: Cliente-Servidor-Base de Datos

## 🔒 Notas de Seguridad

- ⚠️ **NUNCA** subas `testvscode.json` a control de versiones
- ⚠️ **NUNCA** subas el archivo `.env` a control de versiones
- Añade estos archivos a `.gitignore`:
  ```
  testvscode.json
  .env
  __pycache__/
  *.pyc
  ```

## 🎯 Uso Educativo

Esta aplicación está diseñada para:

- **Estudiantes**: Aprender Flask y Firebase de forma interactiva
- **Profesores**: Usar como material de enseñanza
- **Desarrolladores**: Entender la integración Flask + Firebase

## 📝 Rutas Disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal con lista de usuarios |
| `/add_user` | POST | Añade un nuevo usuario a Firebase |
| `/delete_user/<id>` | POST | Elimina un usuario de Firebase |
| `/tutorial` | GET | Vista de tutorial interactivo |
| `/practice` | GET | Vista de ejercicios prácticos |

## 🐛 Solución de Problemas

### Error: Firebase no inicializado
- Verifica que el archivo `testvscode.json` existe y está en la raíz del proyecto
- Verifica que `DATABASE_URL` en `.env` es correcta

### Error: Módulo no encontrado
- Ejecuta `pip install -r requirements.txt` para instalar todas las dependencias

### Error: Puerto ya en uso
- Cambia el puerto en `main.py`: `app.run(debug=True, port=5001)`

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de:
- Reportar bugs
- Sugerir nuevas funcionalidades
- Mejorar la documentación
- Añadir más ejercicios o tutoriales

## 📧 Contacto

Para preguntas o sugerencias sobre este proyecto educativo.

---

**¡Disfruta aprendiendo Flask y Firebase!** 🚀
