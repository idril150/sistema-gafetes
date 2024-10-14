from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import win32api
import win32print

# Función para agregar texto al PDF con una imagen de fondo
def crear_pdf_con_imagen(fondo, nombre, edad, id_numero, salida_pdf):
    # Cargamos la imagen de fondo
    imagen_fondo = Image.open(fondo)
    ancho = 245
    alto = 267

    # Crear el PDF en la escala adecuada
    c = canvas.Canvas(salida_pdf, pagesize=(ancho, alto))

    # Dibujar la imagen de fondo en el PDF
    c.drawImage(fondo, 0, 0, width=ancho, height=alto)
    
    # Dibujar un rectángulo
    c.setFillColorRGB(255, 255, 255)  # Color del rectángulo (blanco en este caso)
    c.roundRect(5, 190, 200, 30, 10, stroke=1, fill=1)  # (x, y, ancho, alto, radio)

    # Añadir el texto en las coordenadas deseadas (x, y)
    c.setFont("Helvetica", 10)  # Cambia el tipo de letra y tamaño aquí
    c.setFillColorRGB(69 / 255, 86 / 255, 243 / 255)

    # Ajusta la posición (x, y) para que esté visible en el PDF
    c.drawString(10, 200, nombre)
    c.drawString(10, 170, edad)
    c.drawString(10, 140, id_numero)

    # Guardar el PDF
    c.save()

    # Enviar el PDF a imprimir
"""     imprimir_pdf(salida_pdf)

def imprimir_pdf(pdf_file):
    # Obtener la impresora predeterminada
    printer_name = win32print.GetDefaultPrinter()

    # Enviar el archivo PDF a imprimir
    win32api.ShellExecute(0, "print", pdf_file, None, ".", 0) """

# Si este archivo es ejecutado directamente (por ejemplo, para pruebas)
if __name__ == "__main__":
    # Datos de prueba (puedes comentarlos si solo quieres usar el escáner)
    imagen_fondo = "C:/Users/Soporte/Pictures/xd.jpg"  # Imagen de fondo
    nombre = "victor"
    edad = "25"
    id_numero = "125"
    salida_pdf = "salida_con_imagen_fondo.pdf"  # Nombre del archivo PDF de salida

    # Crear el PDF
    crear_pdf_con_imagen(imagen_fondo, nombre, edad, id_numero, salida_pdf)
