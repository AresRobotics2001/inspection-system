# Automated Visual Inspection System (Simulated)

This project implements a **simulated industrial visual inspection system** using
computer vision techniques and a client–server architecture.

The system analyzes images captured from a simulated camera, compares them against
a reference part using **SSIM (Structural Similarity Index)**, and determines whether
the inspected piece is acceptable or defective.

---

## Project Features

- Simulated camera capturing images from a production line
- Backend API built with **FastAPI**
- Image processing using **OpenCV**
- Structural similarity analysis (SSIM)
- Defect detection based on configurable thresholds
- Inspection result logging for traceability
- Architecture prepared for future actuator integration

---

## System Architecture

```text
Camera Simulator → FastAPI Backend → Vision Analysis → Inspection Result

🛠 Technologies Used

Python 3
FastAPI
OpenCV
NumPy
scikit-image
Uvicorn

▶️ How to Run the Project

1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
pip install -r requirements.txt

3. Start backend server
uvicorn backend.main:app --reload

4. Run camera simulator
python simulator/camera_simulator.py

📊 Output

Each inspected image generates:
SSIM value
Inspection result (OK / DEFECT)
Optional inspection log (CSV)

🚀 Future Improvements

Integration of simulated or real industrial actuators
Dashboard for inspection statistics
Machine learning–based defect classification
PLC / Arduino communication

📄 License

This project is for educational and portfolio purposes.
