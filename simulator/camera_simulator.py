import os
import time
import requests
import csv
from datetime import datetime

API_URL = "http://127.0.0.1:8000/analyze"
INPUT_FOLDER = "input_stream"
DELAY_SECONDS = 3
LOG_FILE = "inspection_log.csv"


def log_result(image_name, ssim_value, result):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "image", "ssim", "result"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            image_name,
            round(ssim_value, 3),
            result
        ])


def simulate_camera():
    images = sorted(os.listdir(INPUT_FOLDER))

    for img_name in images:
        if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        img_path = os.path.join(INPUT_FOLDER, img_name)

        print(f"📸 Capturando imagen: {img_name}")

        with open(img_path, "rb") as img_file:
            files = {"file": img_file}
            response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            data = response.json()
            result = data["result"]
            ssim = data["ssim"]

            print(f"✅ Resultado: {result} (SSIM={ssim:.2f})")

            log_result(img_name, ssim, result)
        else:
            print("❌ Error en la inspección")

        time.sleep(DELAY_SECONDS)


if __name__ == "__main__":
    simulate_camera()
