import cv2
from ultralytics import YOLO

# 1. Cargar el modelo pre-entrenado
# Al poner "yolov8n.pt", descargará automáticamente la versión "Nano" (la más ligera y rápida)
print("Cargando el modelo...")
model = YOLO("yolov8n.pt") 

# 2. Iniciar la cámara web (el '0' suele ser la cámara integrada de tu laptop)
cap = cv2.VideoCapture(0)

print("Iniciando cámara... Presiona la tecla 'q' en la ventana del video para salir.")

while True:
    # Leer el frame (imagen) actual de la cámara
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo acceder a la cámara.")
        break

    # 3. Hacer la predicción (inferencia) sobre el frame
    # stream=True lo hace más eficiente para flujos continuos como video
    resultados = model(frame, stream=True)

    # 4. Dibujar las cajas delimitadoras y etiquetas en el frame
    for r in resultados:
        # El método plot() dibuja automáticamente todo sobre la imagen original
        annotated_frame = r.plot()

    # 5. Mostrar el video resultante en una ventana
    cv2.imshow("Detector YOLOv8", annotated_frame)

    # 6. Condición de salida: presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpiar los recursos al terminar
cap.release()
cv2.destroyAllWindows()