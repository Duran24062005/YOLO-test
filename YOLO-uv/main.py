from ultralytics import YOLO

# Cargar un modelo preentrenado
model = YOLO("yolov8n.pt")

# Ejecutar inferencia en una imagen
results = model("https://ultralytics.com")

# Mostrar resultados en pantalla
for result in results:
    result.show()
