# 📁 Archive Project

**Archive Project** es una herramienta desarrollada para asistir a estudiantes y docentes en la gestión y conversión de archivos educativos. Automatiza tareas comunes como la descarga de contenido desde YouTube y la transformación de archivos en formatos útiles para clases o tareas.

---

## 🧩 Características Principales

- 🎬 **Descarga de videos o audios desde YouTube** (con `pytube`)
- 📄 **Conversión de `.docx` a `.pdf`** (con `docx2pdf`)
- 📝 **Generación de PDFs desde texto** (con `fpdf`)
- 🖼️ **Conversión de imágenes a PDF y procesamiento básico** (con `Pillow`)
- 📄📄 **Unión de PDFs en uno solo** (con `PyPDF2`)

---

## 🛠️ Requisitos

### 📦 Dependencias

Asegúrate de tener Python instalado. Luego instala las siguientes bibliotecas:

```bash
pip install pytube docx2pdf fpdf pillow PyPDF2

| Paquete    | Función                                   |
| ---------- | ----------------------------------------- |
| `pytube`   | Descarga de videos desde YouTube          |
| `docx2pdf` | Conversión de documentos `.docx` a `.pdf` |
| `fpdf`     | Creación de documentos PDF                |
| `Pillow`   | Manipulación de imágenes                  |
| `PyPDF2`   | Fusionar paginas de PDFs                  |
