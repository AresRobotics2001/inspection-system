import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from pathlib import Path

# Imagen patrón
REFERENCE_IMAGE_PATH = Path("vision/reference/pieza_ok.png")

# Umbrales industriales
THRESHOLD_OK = 0.90
THRESHOLD_WARNING = 0.85


def analyze_image(image_bytes):

    """
    Analiza una imagen contra la referencia y devuelve
    una decisión estructurada (lista para actuadores).
    """

    # --- Decodificar imagen recibida ---
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img_test = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    if img_test is None:
        return {
            "error": "Imagen inválida"
        }

    # --- Cargar imagen patrón ---
    img_ref = cv2.imread(str(REFERENCE_IMAGE_PATH), cv2.IMREAD_GRAYSCALE)

    if img_ref is None:
        return {
            "error": "Imagen patrón no encontrada"
        }

    # --- Normalizar tamaño ---
    img_test = cv2.resize(img_test, (img_ref.shape[1], img_ref.shape[0]))

    # --- Calcular SSIM ---
    similarity, _ = ssim(img_ref, img_test, full=True)
    similarity = float(similarity)

    # --- Clasificación industrial ---
    if similarity >= THRESHOLD_OK:
        classification = "OK"
        actuator = "PASS"

    elif similarity >= THRESHOLD_WARNING:
        classification = "DEFECTO_LEVE"
        actuator = "ALERT"

    else:
        classification = "DEFECTO_CRITICO"
        actuator = "REJECT"

    return {
        "ssim": round(similarity, 3),
        "classification": classification,
        "actuator": actuator
    }
#


