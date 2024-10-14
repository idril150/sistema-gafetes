import cv2
from pyzbar.pyzbar import decode
import numpy as np
import time
import gafetes  # Importar el módulo gafetes

def escanear_qr():
    # Abrir la cámara
    cap = cv2.VideoCapture(0)
    escaneo_habilitado = True  # Variable para controlar el escaneo

    while True:
        # Capturar frame por frame
        ret, frame = cap.read()
        
        # Decodificar los códigos QR en el frame solo si el escaneo está habilitado
        if escaneo_habilitado:
            try:
                decoded_objects = decode(frame)
            except Exception as e:
                print(f"Error al decodificar: {e}")
                continue
            # Dibujar los códigos QR y almacenar el texto
            qr_text = ""
            for obj in decoded_objects:
                (x, y, w, h) = obj.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                qr_text = obj.data.decode('utf-8')  # Guardar el texto del código QR

                # Procesar el texto QR
                if qr_text.startswith("{") and qr_text.endswith("}"):
                    contenido = qr_text[1:-1]  # Quitar las llaves
                    nombre, edad, id_numero = contenido.split(";")  # Separar por ';'
                    
                    # Enviar datos a gafetes.py
                    imagen_fondo = "C:/Users/Soporte/Pictures/xd.jpg"  # Cambia la ruta de la imagen de fondo según sea necesario
                    salida_pdf = f"{nombre}{edad}.pdf"  # Nombre del archivo PDF de salida
                    gafetes.crear_pdf_con_imagen(imagen_fondo, nombre, edad, id_numero, salida_pdf)                    
        # Crear un recuadro para mostrar la cámara
        frame_resized = cv2.resize(frame, (640, 480))
        
        # Crear un recuadro para mostrar el texto
        texto_frame = np.zeros((100, 640, 3), dtype=np.uint8)  # Crear una imagen negra para el texto
        cv2.putText(texto_frame, qr_text if qr_text else "Esperando QR...", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Mostrar ambos recuadros
        cv2.imshow('Escaneo QR', frame_resized)
        #cv2.imshow('Información del QR', texto_frame)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura y cerrar ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para escanear QR
escanear_qr()
