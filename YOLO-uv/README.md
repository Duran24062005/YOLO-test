Para instalar y ejecutar YOLO (Ultralytics) localmente usando uv (el instalador ultra rápido de Python), debes inicializar un proyecto, añadir la librería oficial y ejecutar el comando de predicción a través del entorno virtual automatizado de uv.
Aquí tienes los pasos secuenciales para lograrlo de forma inmediata:
## 1. Inicializar el proyecto
Crea una carpeta para tu proyecto y genera el entorno gestionado por uv:

mkdir mi-yolo && cd mi-yolo
uv init

## 2. Instalar Ultralytics
Añade el paquete oficial de YOLO a las dependencias de tu proyecto:

uv add ultralytics

(Nota: uv descargará automáticamente la versión de PyTorch adecuada para tu sistema).
## 3. Descargar un modelo y probarlo
Puedes ejecutar YOLO directamente desde la terminal sin activar manualmente el entorno virtual usando uv run:

uv run yolo predict model=yolov8n.pt source='https://ultralytics.com'

## 4. Ejecutar mediante un script de Python
Si prefieres programar tu propia lógica, crea un archivo llamado script.py:

from ultralytics import YOLO
# Cargar un modelo preentrenadomodel = YOLO("yolov8n.pt")
# Ejecutar inferencia en una imagenresults = model("https://ultralytics.com")
# Mostrar resultados en pantallafor result in results:
    result.show()

Ejecuta tu script con el comando:

uv run script.py

------------------------------
Si quieres profundizar en tu desarrollo, te puedo ayudar a configurar más opciones. Dime si prefieres:

* Configurar el entorno para que use tu tarjeta gráfica (GPU / CUDA).
* Crear un script para procesar video en tiempo real desde tu cámara web.
* Preparar el proyecto para entrenar un modelo propio con tus imágenes.


