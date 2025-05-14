import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert
from fpdf import FPDF
import os
from PIL import Image
from PyPDF2 import PdfMerger

# Seleccionar el archivo que se utilizará
def escojer_archivo(nombre_tipo_documento, extension_archivo):
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[(nombre_tipo_documento, extension_archivo)],
    )
    if ruta_archivo:
        print("Archivo seleccionado:", ruta_archivo)
        return ruta_archivo
    else:
        print("No se seleccionó ningún archivo.")
        return None

# Convertir el archivo .txt a .pdf
def txt_a_pdf(ruta_txt, ruta_pdf):
    if not os.path.exists(ruta_txt):
        print(f"El archivo de texto {ruta_txt} no existe.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Abrimos el archivo de texto
    with open(ruta_txt, "r", encoding="utf-8") as file:
        for linea in file:
            pdf.cell(200, 10, txt=linea.strip(), ln=1)

    pdf.output(ruta_pdf)
    print(f"PDF creado correctamente: {ruta_pdf}")

# Convertir archivo de texto a PDF
def texto_a_pdf():
    nombre_tipo_documento = "Archivo de texto"
    extension_archivo = "*.txt"
    ruta_archivo = escojer_archivo(nombre_tipo_documento, extension_archivo)
    if ruta_archivo:
        try:
            salida_pdf = os.path.splitext(ruta_archivo)[0] + ".pdf"
            txt_a_pdf(ruta_archivo, salida_pdf)
        except Exception as e:
            print("Error al convertir el archivo:", e)
    else:
        print("Archivo no encontrado")

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

# Convertir imagen a pdf
def img_a_pdf():
    nombre_tipo_documento = "Imagen"
    extension_archivo = "*.jpg"
    ruta_archivo = escojer_archivo(nombre_tipo_documento, extension_archivo)
    if ruta_archivo:
        try:
            imagen = Image.open(ruta_archivo)
            salida_pdf = os.path.splitext(ruta_archivo)[0] + ".pdf"
            imagen.convert("RGB").save(salida_pdf)
            print("Imagen convertida a PDF correctamente.")
        except Exception as e:
            print("Error al convertir el archivo:", e)
    else:
        print("Archivo no encontrado")

# Unir varios PDFs
def unir_pdfs():
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)

    print("Abriendo selector de archivos PDF...")
    rutas_archivos = filedialog.askopenfilenames(
        title="Selecciona los archivos PDF que deseas unir",
        filetypes=[("Archivos PDF", "*.pdf")],
        parent=root
    )

    if not rutas_archivos:
        print("No se seleccionaron archivos.")
        return

    merger = PdfMerger()
    for pdf in rutas_archivos:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Error al agregar {pdf}: {e}")

    print("Abriendo ventana para guardar el archivo final...")
    salida = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Archivo PDF", "*.pdf")],
        title="Guardar PDF combinado como",
        parent=root
    )

    if salida:
        merger.write(salida)
        merger.close()
        print(f"PDFs combinados correctamente en: {salida}")
    else:
        print("Operación cancelada.")


# Menú principal
print("Seleccione una opción")
print("1.- Convertir un archivo a PDF")
print("2.- Unir varios PDF")
opc = int(input("Opción: "))

if opc == 1:
    print("Seleccione el tipo de archivo que desea convertir a PDF")
    print("1.- Documento Word")
    print("2.- Documento texto (txt)")
    print("3.-Convertir imagen a pdf")
    sub_opc = int(input("Opción: "))
    if sub_opc == 1:
        word_a_pdf()
    elif sub_opc == 2:
        texto_a_pdf()
    elif sub_opc == 3:
        img_a_pdf()
elif opc == 2:
    unir_pdfs()

