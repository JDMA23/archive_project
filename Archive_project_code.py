import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert

# Seleccionar el archivo que se utilizará
def escojer_archivo(nombre_tipo_documento, extension_archivo):
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[
            (nombre_tipo_documento, extension_archivo),
        ]
    )
    if ruta_archivo:
        print("Archivo seleccionado:", ruta_archivo)
        return ruta_archivo
    else:
        print("No se seleccionó ningún archivo.")
        return None

# Convertir el archivo Word a PDF
def word_a_pdf():
    nombre_tipo_documento = "Documento Word"
    extension_archivo = "*.docx"
    ruta_archivo = escojer_archivo(nombre_tipo_documento, extension_archivo)
    if ruta_archivo:
        try:
            convert(ruta_archivo)
            print("¡Documento convertido a PDF correctamente!")
        except Exception as e:
            print("Error al convertir el archivo:", e)
    else:
        print("Archivo no encontrado")

# Menú principal
print("Seleccione una opción")
print("1.- Convertir documento a PDF")
opc = int(input("Opción: "))

if opc == 1:
    print("Seleccione el tipo de archivo que desea convertir a PDF")
    print("1.- Documento Word")
    sub_opc = int(input("Opción: "))
    if sub_opc == 1:
        word_a_pdf()
